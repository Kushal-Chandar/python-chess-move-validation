from pieces import Piece
from typing import Tuple


class Square:
    piece: Piece | None
    position: Tuple[int, int]
    # additional attributes like, can promote ?
    def __init__(self, position: Tuple[int, int], piece: Piece = None) -> None:
        self.piece = piece
        self.position = position

    def addPiece(self, piece: Piece):
        self.piece = piece

    def __str__(self):
        print = self.piece if self.piece else " "
        piece_str = f" {print} |"
        if self.position[1] == 0:
            piece_str = "|" + piece_str
        return piece_str
