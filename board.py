from square import Square
from pieces import Piece
from typing import List


class Board:
    board: List[List[Square]] = []
    size = (8, 8)

    def __init__(self) -> None:
        self.board = []
        for i in range(self.size[0]):
            temp = []
            for j in range(self.size[1]):
                temp.append(Square((i, j)))
            self.board.append(temp)

    def addPiece(self, piece: Piece):
        i, j = piece.position
        self.board[i][j].addPiece(piece)

    def __str__(self):
        board = ""
        for row in self.board:
            board += "---------------------------------"
            board += "\n"
            for item in row:
                board += str(item)
            board += "\n"
        board += "---------------------------------"
        return board

    def board_index(self):
        board = ""
        for i, _ in enumerate(self.board):
            board += "---------------------------------------------------------"
            board += "\n"
            for j, _ in enumerate(self.board[i]):
                board += str(f"|({i}, {j})")
            board += "|\n"
        board += "---------------------------------------------------------"
        return board
