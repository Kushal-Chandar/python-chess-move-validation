from typing import List, Tuple, Set
from typing_chess import Square, Board


class Piece:
    position: Tuple[int, int] | None

    def __init__(self, position: Tuple[int, int]):
        self.position = position

    def getValidMoves(self, board: Board, position: Square) -> List[Square]:
        print("Piece Not Specified")
        return []

    @staticmethod
    def isInBoard(board: Board, position: List[int]):
        [x, y] = position
        if not (
            x >= 0 and x <= board.size[0] - 1 and y >= 0 and y <= board.size[1] - 1
        ):
            return False
        return True

    @staticmethod
    def getValidOperation(
        board: List[List[Square]], position: Square, operation: Tuple[int, int]
    ) -> Tuple[int, int] | None:
        current_position = [position.position[0], position.position[1]]
        current_position[0] += operation[0]
        current_position[1] += operation[1]
        if (
            not Piece.isInBoard(board, current_position)
            or board.board[current_position[0]][current_position[1]].piece
        ):
            return None
        return tuple(current_position)

    @staticmethod
    def getAllValidMovesForOperations(
        board: Board,
        position: Square,
        operations: List[Tuple[int, int]],
        getOne: bool = False,
    ) -> Set[Tuple[int, int]]:
        valid_moves = set()
        i = 1
        trackings = [True] * len(operations)
        while True:
            for k in range(len(operations)):
                if not trackings[k]:
                    continue
                op = Piece.ValidOperation(
                    board, position, (operations[k][0] * i, operations[k][1] * i)
                )
                if op:
                    valid_moves.add(op)
                else:
                    trackings[k] = False

            for tracking in trackings:
                if tracking:
                    break
            else:
                break

            i += 1

            if getOne:
                break

        return valid_moves

    def getValidMoves(self, board: Board, position: Square) -> Set[Tuple[int, int]]:
        return Piece.getAllValidMovesForOperations(
            board, position, self.operations, self.oneMove
        )

    def __str__(self):
        return f"-"


class Pawn(Piece):
    operations = [(1, 0)]
    oneMove = True

    def __str__(self):
        return f"P"


class Knight(Piece):
    operations = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (-1, 2),
        (1, -2),
        (-1, -2),
    ]
    oneMove = True

    def __str__(self):
        return f"N"


class Rook(Piece):
    operations = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    oneMove = False

    def __str__(self):
        return f"R"


class Bishop(Piece):
    operations = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    oneMove = False

    def __str__(self):
        return f"B"


class Queen(Piece):
    operations = [
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]
    oneMove = False

    def __str__(self):
        return f"Q"


class King(Piece):
    operations = [
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]
    oneMove = True

    def __str__(self):
        return f"K"
