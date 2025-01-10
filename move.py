class Move:
    """
        Represents a move from one square to another square.

        Attributes:
            initial : The initial square of the move.
            final : The final square of the move.
    """
    def __init__(self, initial, final):
        self.initial = initial
        self.final = final

    def __str__(self):
        move_representation = ''
        move_representation += f'({self.initial.col}, {self.initial.row} -> ({self.final.col}, {self.final.row})'
        return move_representation

    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final

