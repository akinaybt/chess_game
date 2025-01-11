import pygame
import sys


from board import Board
from const import *
from game import Game
from minimax import Minimax

from square import Square
from move import Move
from move_operations import CalculateMoves




class Main:
    """
       The main application class for the chess game. It initializes the game, handles user interactions,
       and manages the main event loop for rendering the game and processing input.

       Attributes:
           icon : The application icon loaded from an image file.
           screen : The main display surface for the game.
           game (Game): The core game logic and state manager.
           board (Board): The chessboard, managing the state of pieces and moves.
           dragger (Dragger): The piece drag-and-drop manager.

       Methods:
           mainloop():
               Runs the main event loop for the game, handling user input and updating the display.
       """
    icon = pygame.image.load('imgs/chessimg.png')
    pygame.display.set_icon(icon)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()
        self.board = self.game.board
        self.dragger = self.game.dragger
        self.ai_mode = False

    def mainloop(self):

        while True:
            # Show methods
            self.game.show_bg(self.screen)
            self.game.show_last_move(self.screen)
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
                            CalculateMoves.calculate_move(piece, clicked_row, clicked_col, self.board)
                            self.dragger.save_initial_position(event.pos)
                            self.dragger.drag_piece(piece)
                            # Show methods
                            self.game.show_bg(self.screen)
                            self.game.show_last_move(self.screen)
                            self.game.show_moves(self.screen)
                            self.game.show_pieces(self.screen)

                # Mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if self.dragger.dragging:
                        self.dragger.update_mouse_coordinate(event.pos)
                        # Show methods
                        self.game.show_bg(self.screen)
                        self.game.show_last_move(self.screen)
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

                        if not Square.is_within_bounds(released_row, released_col):
                            self.dragger.return_piece()
                        else:
                            # Creating a possible move
                            initial = Square(self.dragger.initial_row, self.dragger.initial_col)
                            final = Square(released_row, released_col)
                            move = Move(initial, final)

                            # Checking if the move is valid
                            if self.board.valid_move(self.dragger.piece, move):
                                captured = self.board.squares[released_row][released_col].has_piece()
                                self.board.move(self.dragger.piece, move)
                                print(self.dragger.initial_row, self.dragger.initial_col)

                                # Sounds
                                self.game.play_sound(captured)
                                # Show methods
                                self.game.show_bg(self.screen)
                                self.game.show_moves(self.screen)
                                self.game.show_pieces(self.screen)
                                self.game.next_turn()

                                # AI move
                                if self.ai_mode and self.game.next_player == 'black':
                                    _, best_move = Minimax.minimax(self.board, 4, -float('inf'), float('inf'), True)
                                    if best_move:
                                        print(best_move)
                                        self.board.move(self.board.squares[best_move.initial.row][best_move.initial.col].piece, best_move)
                                        self.game.next_turn()
                                        # Добавьте вызов методов отображения после хода AI
                                        self.game.show_bg(self.screen)
                                        self.game.show_last_move(self.screen)
                                        self.game.show_moves(self.screen)
                                        self.game.show_pieces(self.screen)
                                    else :
                                        pygame.quit()
                                        sys.exit()

                                if self.board.game_over(self.board):
                                    pygame.quit()
                                    sys.exit()

                    self.dragger.undrag_piece()

                # Quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


# Mode selection
print("Select game mode:")
print("1. Player vs Player")
print("2. Player vs AI")
mode = input("Enter your choice (1/2): ")

main = Main()
if mode == '2':
    main.ai_mode = True
main.mainloop()