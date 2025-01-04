from bishop import Bishop
from king import King
from knight import Knight
from pawn import Pawn
from rook import Rook
from queen import Queen
from square import Square
from board import Board
from move import Move

class CalculateMoves:
    """ Class CalculateMove is designed to calculate all possible moves for pieces. """
    @staticmethod
    def calculate_move(piece, row, col):
        board = Board()
        def knight_moves():
            knight_possible_moves = [
                (row - 2, col + 1),
                (row - 1, col + 2),
                (row + 1, col + 2),
                (row + 2, col + 1),
                (row + 2, col - 1),
                (row + 1, col - 2),
                (row - 1, col - 2),
                (row - 2, col - 1),

            ]

            for possible_move in knight_possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.is_within_bounds(possible_move_row, possible_move_col):
                    if board.squares[possible_move_row][possible_move_col].empty_or_rival(piece.colour):
                        # Creating a square for a new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # Creating and appending a new valid move
                        move = Move(initial, final)
                        piece.add_move(move)

        def pawn_moves():
            # Checking if a pawn made the first move or not
            steps = 1 if piece.made_move else 2

            # Possible vertical moves
            start = row + piece.direction
            end = row + (piece.direction * (steps + 1 ))

            for possible_move_row in range(start, end, piece.direction):
                if Square.is_within_bounds(possible_move_row):
                    if board.squares[possible_move_row][col].is_empty():
                        # Creating an initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        # Creating and appending a new move
                        move = Move(initial, final)
                        piece.add_move(move)

                    # If a square is not empty, it is blocked
                    else: break
                # If a square is not in range
                else: break

            # Possible diagonal moves
            possible_move_row = row + piece.direction
            possible_move_cols = [col - 1, col + 1]

            for possible_move_col in possible_move_cols:
                if Square.is_within_bounds(possible_move_row, possible_move_col):
                    if board.squares[possible_move_row][possible_move_col].has_rival_piece(piece.colour):
                        # Creating an initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # Creating and appending a new move
                        move = Move(initial, final)
                        piece.add_move(move)

        def straight_line_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.is_within_bounds(possible_move_row, possible_move_col):

                        # Checking if a square is empty, then it will continue looping
                        if board.squares[possible_move_row][possible_move_col].is_empty():
                            # Creating and appending squares of a new possible move
                            initial = Square(row, col)
                            final = Square(possible_move_row, possible_move_col)
                            move = Move(initial, final)
                            piece.add_move(move)

                        # Checking if a square has an enemy piece
                        if board.squares[possible_move_row][possible_move_col].has_rival_piece(piece.colour):
                            # Creating and appending squares of a new possible move
                            initial = Square(row, col)
                            final = Square(possible_move_row, possible_move_col)
                            move = Move(initial, final)
                            piece.add_move(move)
                            break

                        # Checking if a square has a team piece, then it will break
                        if board.squares[possible_move_row][possible_move_col].has_team_piece(piece.colour):
                            break

                    else:
                        break

                    # Changing the increments
                    possible_move_row += row_incr
                    possible_move_col += col_incr

        def king_moves():
            king_possible_moves = [
                (row - 1, col + 0),
                (row - 1, col + 1),
                (row + 0, col + 1),
                (row + 1, col + 1),
                (row + 1, col + 0),
                (row + 1, col - 1),
                (row + 0, col - 1),
                (row - 1, col - 1)
            ]

            # King's ordinary moves
            for possible_move in king_possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.is_within_bounds(possible_move_row, possible_move_col):
                    if board.squares[possible_move_row][possible_move_col].empty_or_rival(piece.colour):
                        # Creating a square for a new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # Creating and appending a new valid move
                        move = Move(initial, final)
                        piece.add_move(move)

        if isinstance(piece, Pawn):
            pawn_moves()
        elif isinstance(piece, Knight):
            knight_moves()
        elif isinstance(piece, Bishop):
            bishop_moves = [
                (-1, 1), (-1, -1), (1, 1), (1, -1)
            ]
            straight_line_moves(bishop_moves)
        elif isinstance(piece, Rook):
            rook_moves = [
                (-1, 0), (1, 0), (0, -1), (0, 1)
            ]
            straight_line_moves(rook_moves)
        elif isinstance(piece, Queen):
            queen_moves = [
                (-1, 1), (-1, -1), (1, 1), (1, -1),
                (-1, 0), (1, 0), (0, -1), (0, 1)
            ]
            straight_line_moves(queen_moves)
        elif isinstance(piece, King):
            king_moves()
