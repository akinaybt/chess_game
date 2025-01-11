from move_operations import CalculateMoves
from square import Square
from board import Board


class ChessBoard:
    def __init__(self, board, is_white_turn):
        self.board = board
        self.is_white_turn = is_white_turn

    def generate_legal_moves(self):
        legal_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board.squares[row][col].piece
                if piece and piece.colour == ('white' if self.is_white_turn else 'black'):
                    CalculateMoves.calculate_move(piece, row, col, self.board)
                    legal_moves.extend(piece.moves)
                    piece.clear_moves()
        return legal_moves

    def make_move(self, move):
        initial = move.initial
        final = move.final

        prev_piece = self.board.squares[final.row][final.col].piece
        moved_piece = self.board.squares[initial.row][initial.col].piece

        self.board.squares[final.row][final.col].piece = moved_piece
        self.board.squares[initial.row][initial.col].piece = None

        self.is_white_turn = not self.is_white_turn
        return (move, prev_piece)

    def undo_move(self, move_info):
        move, prev_piece = move_info
        initial = move.initial
        final = move.final

        self.board.squares[initial.row][initial.col].piece = self.board.squares[final.row][final.col].piece
        self.board.squares[final.row][final.col].piece = prev_piece

        self.is_white_turn = not self.is_white_turn

    def is_game_over(self):
        # Используем корректный вызов game_over для объекта board
        return self.board.game_over()

    def evaluate(self):
        piece_values = {
            'pawn': 1,
            'knight': 3,
            'bishop': 3,
            'rook': 5,
            'queen': 9,
            'king': 0  # King is invaluable
        }

        score = 0
        for row in self.board.squares:
            for square in row:
                piece = square.piece
                if piece:
                    value = piece_values[piece.name]
                    score += value if piece.colour == 'white' else -value
        return score


class Minimax:
    @staticmethod
    def minimax(chess_board, depth, alpha, beta, maximizing_player):
        # Исправляем вызов is_game_over
        if depth == 0 or chess_board.is_game_over():
            return chess_board.evaluate(), None

        best_move = None

        if maximizing_player:
            max_eval = float('-inf')
            for move in chess_board.generate_legal_moves():
                move_info = chess_board.make_move(move)
                _eval, _ = Minimax.minimax(chess_board, depth - 1, alpha, beta, False)
                chess_board.undo_move(move_info)

                if _eval > max_eval:
                    max_eval = _eval
                    best_move = move
                alpha = max(alpha, _eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in chess_board.generate_legal_moves():
                move_info = chess_board.make_move(move)
                _eval, _ = Minimax.minimax(chess_board, depth - 1, alpha, beta, True)
                chess_board.undo_move(move_info)

                if _eval < min_eval:
                    min_eval = _eval
                    best_move = move
                beta = min(beta, _eval)
                if beta <= alpha:
                    break
            return min_eval, best_move
