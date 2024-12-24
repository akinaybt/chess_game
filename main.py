import pygame
import sys
from const import *
from game import Game


class Main:

    icon = pygame.image.load('imgs/chessimg.png')
    pygame.display.set_icon(icon)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()
        self.board = self.game.board
        self.dragger = self.game.dragger

    def mainloop(self):

        while True:
            self.game.show_bg(self.screen)
            self.game.show_pieces(self.screen)

            if self.dragger.dragging:
                self.dragger.update_position(self.screen)

            for event in pygame.event.get():

                # Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.dragger.update_mouse_coordinate(event.pos)

                    clicked_row = self.dragger.y_coordinate // SQSIZE
                    clicked_col = self.dragger.x_coordinate // SQSIZE

                    # The method checks if the square has a piece
                    if self.board.squares[clicked_row][clicked_col].has_piece():
                        piece = self.board.squares[clicked_row][clicked_col].piece
                        self.dragger.save_initial_position(event.pos)
                        self.dragger.drag_piece(piece)

                # Mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if self.dragger.dragging:
                        self.dragger.update_mouse_coordinate(event.pos)
                        self.game.show_bg(self.screen)
                        self.game.show_pieces(self.screen)
                        self.dragger.update_position(self.screen)

                # Click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.dragger.undrag_piece()

                # Quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()