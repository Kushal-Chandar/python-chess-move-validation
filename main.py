from square import Square
from typing import Set
from pieces import Rook, Pawn, Queen, Bishop, King, Knight
from board import Board


def GetValidMoves(board: Board, position: Square) -> Set[Square]:
    if position.piece:
        return position.piece.getValidMoves(board, position)
    return []


def isValidMove(board: Board, start: Square, end: Square):
    valid_moves = GetValidMoves(
        board, board.board[start.position[0]][start.position[1]]
    )
    return end.position in valid_moves


def BishopTest():
    board = Board()
    board.addPiece(Bishop((4, 4)))
    board.addPiece(Rook((1, 1)))
    board.addPiece(Rook((3, 3)))
    board.addPiece(Rook((3, 5)))
    print("Before Validation")
    print(board)
    valid = "" if isValidMove(board, Square((4, 4)), Square((0, 0))) else "not"
    print(f"The move from (4, 4) to (0, 0) is {valid} valid")
    board2 = Board()
    board2.addPiece(Bishop((4, 4)))
    board2.addPiece(Rook((1, 1)))
    board2.addPiece(Rook((3, 3)))
    board2.addPiece(Rook((3, 5)))
    valid_moves = GetValidMoves(board, board.board[4][4])
    for valid_move in valid_moves:
        board2.addPiece(Bishop(valid_move))
    print("After Validation")
    print(board2)


def RookTest():
    board = Board()
    board.addPiece(Rook((4, 4)))
    board.addPiece(Pawn((1, 1)))
    board.addPiece(Pawn((3, 3)))
    board.addPiece(Pawn((3, 5)))
    board.addPiece(Pawn((4, 3)))
    board.addPiece(Pawn((5, 4)))
    print("Before Validation")
    print(board)
    valid = "" if isValidMove(board, Square((4, 4)), Square((0, 4))) else "not"
    print(f"The move from (4, 4) to (0, 4) is {valid} valid")
    board2 = Board()
    board2.addPiece(Rook((4, 4)))
    board2.addPiece(Pawn((1, 1)))
    board2.addPiece(Pawn((3, 3)))
    board2.addPiece(Pawn((3, 5)))
    board2.addPiece(Pawn((4, 3)))
    board2.addPiece(Pawn((5, 4)))
    valid_moves = GetValidMoves(board, board.board[4][4])
    for valid_move in valid_moves:
        board2.addPiece(Rook(valid_move))
    print("After Validation")
    print(board2)


def QueenTest():
    board = Board()
    board.addPiece(Queen((4, 4)))
    board.addPiece(Pawn((1, 1)))
    board.addPiece(Pawn((3, 3)))
    board.addPiece(Pawn((3, 5)))
    board.addPiece(Pawn((4, 3)))
    board.addPiece(Pawn((5, 4)))
    print("Before Validation")
    print(board)
    valid = "" if isValidMove(board, Square((4, 4)), Square((7, 7))) else "not"
    print(f"The move from (4, 4) to (7, 7) is {valid} valid")
    board2 = Board()
    board2.addPiece(Queen((4, 4)))
    board2.addPiece(Pawn((1, 1)))
    board2.addPiece(Pawn((3, 3)))
    board2.addPiece(Pawn((3, 5)))
    board2.addPiece(Pawn((4, 3)))
    board2.addPiece(Pawn((5, 4)))
    valid_moves = GetValidMoves(board, board.board[4][4])
    for valid_move in valid_moves:
        board2.addPiece(Queen(valid_move))
    print("After Validation")
    print(board2)


def KingTest():
    board = Board()
    board.addPiece(King((4, 4)))
    board.addPiece(Pawn((1, 1)))
    board.addPiece(Pawn((3, 3)))
    board.addPiece(Pawn((3, 5)))
    board.addPiece(Pawn((4, 3)))
    board.addPiece(Pawn((5, 4)))
    print("Before Validation")
    print(board)
    valid = "" if isValidMove(board, Square((4, 4)), Square((0, 0))) else "not"
    print(f"The move from (4, 4) to (0, 0) is {valid} valid")
    board2 = Board()
    board2.addPiece(King((4, 4)))
    board2.addPiece(Pawn((1, 1)))
    board2.addPiece(Pawn((3, 3)))
    board2.addPiece(Pawn((3, 5)))
    board2.addPiece(Pawn((4, 3)))
    board2.addPiece(Pawn((5, 4)))
    valid_moves = GetValidMoves(board, board.board[4][4])
    for valid_move in valid_moves:
        board2.addPiece(King(valid_move))
    print("After Validation")
    print(board2)


def PawnTest():
    board = Board()
    board.addPiece(Pawn((4, 4)))
    board.addPiece(Bishop((1, 1)))
    board.addPiece(Bishop((3, 3)))
    board.addPiece(Bishop((3, 5)))
    board.addPiece(Bishop((4, 3)))
    # board.addPiece(Bishop((5, 4)))
    print("Before Validation")
    print(board)
    valid = "" if isValidMove(board, Square((4, 4)), Square((0, 0))) else "not"
    print(f"The move from (4, 4) to (0, 0) is {valid} valid")
    board2 = Board()
    board2.addPiece(Pawn((4, 4)))
    board2.addPiece(Bishop((1, 1)))
    board2.addPiece(Bishop((3, 3)))
    board2.addPiece(Bishop((3, 5)))
    board2.addPiece(Bishop((4, 3)))
    # board2.addPiece(Bishop((5, 4)))
    valid_moves = GetValidMoves(board, board.board[4][4])
    for valid_move in valid_moves:
        board2.addPiece(Pawn(valid_move))
    print("After Validation")
    print(board2)


def KnightTest():
    board = Board()
    board.addPiece(Knight((6, 6)))
    board.addPiece(Bishop((1, 1)))
    board.addPiece(Bishop((3, 3)))
    board.addPiece(Bishop((3, 5)))
    board.addPiece(Bishop((4, 3)))
    # board.addPiece(Bishop((5, 4)))
    print("Before Validation")
    print(board)
    valid = "" if isValidMove(board, Square((6, 6)), Square((0, 0))) else "not"
    print(f"The move from (6, 6) to (0, 0) is {valid} valid")
    board2 = Board()
    board2.addPiece(Knight((6, 6)))
    board2.addPiece(Bishop((1, 1)))
    board2.addPiece(Bishop((3, 3)))
    board2.addPiece(Bishop((3, 5)))
    board2.addPiece(Bishop((4, 3)))
    # board2.addPiece(Bishop((5, 4)))
    valid_moves = GetValidMoves(board, board.board[6][6])
    for valid_move in valid_moves:
        board2.addPiece(Knight(valid_move))
    print("After Validation")
    print(board2)


# board = Board()
# print(board.board_index())
# BishopTest()
# RookTest()
# QueenTest()
# KingTest()
# PawnTest()
KnightTest()
