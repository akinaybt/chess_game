import pygame
import sys
from const import *
from game import Game
from square import Square
from move import Move
from move_operations import CalculateMoves

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
            # Show methods
            self.game.show_bg(self.screen)
            self.game.show_moves(self.screen)
            self.game.show_pieces(self.screen)

            if self.dragger.dragging:
                self.dragger.update_position(self.screen)

            for event in pygame.event.get():

                # Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.dragger.update_mouse_coordinate(event.pos)

                    clicked_row = self.dragger.y_coordinate // SQSIZE
                    clicked_col = self.dragger.x_coordinate // SQSIZE

                    # It checks if the square has a piece
                    if self.board.squares[clicked_row][clicked_col].has_piece():
                        piece = self.board.squares[clicked_row][clicked_col].piece
                        if piece.colour == self.game.next_player:
                            CalculateMoves.calculate_move(piece, clicked_row, clicked_col)
                            self.dragger.save_initial_position(event.pos)
                            self.dragger.drag_piece(piece)
                            # Show methods
                            self.game.show_bg(self.screen)
                            self.game.show_moves(self.screen)
                            self.game.show_pieces(self.screen)

                # Mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if self.dragger.dragging:
                        self.dragger.update_mouse_coordinate(event.pos)
                        # Show methods
                        self.game.show_bg(self.screen)
                        self.game.show_moves(self.screen)
                        self.game.show_pieces(self.screen)
                        self.dragger.update_position(self.screen)

                # Click release
                elif event.type == pygame.MOUSEBUTTONUP:

                    if self.dragger.dragging:
                        self.dragger.update_mouse_coordinate(event.pos)

                        # Conversion between the position and the board logical position
                        released_row = self.dragger.y_coordinate // SQSIZE
                        released_col = self.dragger.x_coordinate // SQSIZE

                        # Creating a possible move
                        initial = Square(self.dragger.initial_row, self.dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        # Checking if the move is valid
                        if self.board.valid_move(self.dragger.piece, move):
                            self.board.move(self.dragger.piece, move)

                            # Show methods
                            self.game.show_bg(self.screen)
                            self.game.show_pieces(self.screen)
                            self.game.next_turn()

                    self.dragger.undrag_piece()

                # Quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
