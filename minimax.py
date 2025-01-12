import copy

from board import Board
from const import ROWS, COLS
from move_operations import CalculateMoves
from king import King
from knight import Knight
from pawn import Pawn
from queen import Queen
from rook import Rook
from bishop import Bishop
from square import Square

class ChessBoard:
    def __init__(self, board, is_white_turn):
        # Initializing the board and the current player
        self.board = board
        self.is_white_turn = is_white_turn

    def generate_legal_moves(self):
        # generation of all possible moves for the current player
        legal_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board.squares[row][col].piece
                if piece and piece.colour == ('white' if self.is_white_turn else 'black'):
                    CalculateMoves.calculate_move(piece, row, col, self.board)
                    legal_moves.extend(piece.moves)
                    piece.moves.clear()  # Clearing the move list after use
        return legal_moves

    def make_move(self, move):
        # Performs a move and returns the board state before the move
        initial = move.initial
        final = move.final

        #prev_board_squares = [row[:] for row in self.board.squares]
        prev_board_squares = copy.deepcopy(self.board.squares)
        self.board.squares[final.row][final.col].piece = self.board.squares[initial.row][initial.col].piece
        self.board.squares[initial.row][initial.col].piece = None

        # Change the turn
        self.is_white_turn = not self.is_white_turn
        return prev_board_squares

    def undo_move(self, prev_board_squares):
        # Undoes a move, restoring the previous state of the board.
        self.board.squares = prev_board_squares
        self.is_white_turn = not self.is_white_turn

    def is_game_over(self):
        return self.board.game_over(self.board)

    def evaluate(self):
        # Estimates the current position (simplified estimation)
        score = 0
        for row in self.board.squares:
            for square in row:
                piece = square.piece
                if piece:
                    if piece.colour == 'white':
                        value = piece.value * -1
                    else:
                        value = piece.value
                    score += value
                    #if hash(tuple(tuple(row) for row in self.board.squares)) in self.board.boardhistoryhashes:
                    #    score -= 228
                        #print(str(score) + "old found:" + str(hash(tuple(tuple(row) for row in self.board.squares))))
                    #else:
                        #print(score)
        return score

class Minimax:
    @staticmethod
    def minimax(board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.is_game_over():
            #print(board.board.boardhistoryhashes)
            return board.evaluate(), None

        best_move = None

        if maximizing_player:
            max_eval = float('-inf')
            for move in board.generate_legal_moves():
                prev_board_squares = board.make_move(move)
                eval, _ = Minimax.minimax(board, depth - 1, alpha, beta, False)
                board.undo_move(prev_board_squares)

                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in board.generate_legal_moves():
                prev_board_squares = board.make_move(move)
                eval, _ = Minimax.minimax(board, depth - 1, alpha, beta, True)
                board.undo_move(prev_board_squares)

                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move
