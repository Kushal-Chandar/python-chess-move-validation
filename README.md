# Python Chess Move Validation

[![Python](https://img.shields.io/badge/Python-3776AB?&logo=python&logoColor=white)](https://www.python.org/)

An objected oriented method for validating chess moves.

```Python
board = Board()
print(board.board_index())
```

```Bash
---------------------------------------------------------
|(0, 0)|(0, 1)|(0, 2)|(0, 3)|(0, 4)|(0, 5)|(0, 6)|(0, 7)|
---------------------------------------------------------
|(1, 0)|(1, 1)|(1, 2)|(1, 3)|(1, 4)|(1, 5)|(1, 6)|(1, 7)|
---------------------------------------------------------
|(2, 0)|(2, 1)|(2, 2)|(2, 3)|(2, 4)|(2, 5)|(2, 6)|(2, 7)|
---------------------------------------------------------
|(3, 0)|(3, 1)|(3, 2)|(3, 3)|(3, 4)|(3, 5)|(3, 6)|(3, 7)|
---------------------------------------------------------
|(4, 0)|(4, 1)|(4, 2)|(4, 3)|(4, 4)|(4, 5)|(4, 6)|(4, 7)|
---------------------------------------------------------
|(5, 0)|(5, 1)|(5, 2)|(5, 3)|(5, 4)|(5, 5)|(5, 6)|(5, 7)|
---------------------------------------------------------
|(6, 0)|(6, 1)|(6, 2)|(6, 3)|(6, 4)|(6, 5)|(6, 6)|(6, 7)|
---------------------------------------------------------
|(7, 0)|(7, 1)|(7, 2)|(7, 3)|(7, 4)|(7, 5)|(7, 6)|(7, 7)|
---------------------------------------------------------
```

## Bishop

```Python
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
```

```bash
Before Validation
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   | R |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   | R |   | R |   |   |
---------------------------------
|   |   |   |   | B |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
The move from (4, 4) to (0, 0) is not valid
After Validation
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   | R |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   | R |   | R |   |   |
---------------------------------
|   |   |   |   | B |   |   |   |
---------------------------------
|   |   |   | B |   | B |   |   |
---------------------------------
|   |   | B |   |   |   | B |   |
---------------------------------
|   | B |   |   |   |   |   | B |
---------------------------------
```

## Rook

```Python
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
```

```bash
Before Validation
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   | P |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   | P |   | P |   |   |
---------------------------------
|   |   |   | P | R |   |   |   |
---------------------------------
|   |   |   |   | P |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
The move from (4, 4) to (0, 4) is  valid
After Validation
---------------------------------
|   |   |   |   | R |   |   |   |
---------------------------------
|   | P |   |   | R |   |   |   |
---------------------------------
|   |   |   |   | R |   |   |   |
---------------------------------
|   |   |   | P | R | P |   |   |
---------------------------------
|   |   |   | P | R | R | R | R |
---------------------------------
|   |   |   |   | P |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
```

## Queen

```Python
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
```

```bash
Before Validation
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   | P |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   | P |   | P |   |   |
---------------------------------
|   |   |   | P | Q |   |   |   |
---------------------------------
|   |   |   |   | P |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
The move from (4, 4) to (7, 7) is  valid
After Validation
---------------------------------
|   |   |   |   | Q |   |   |   |
---------------------------------
|   | P |   |   | Q |   |   |   |
---------------------------------
|   |   |   |   | Q |   |   |   |
---------------------------------
|   |   |   | P | Q | P |   |   |
---------------------------------
|   |   |   | P | Q | Q | Q | Q |
---------------------------------
|   |   |   | Q | P | Q |   |   |
---------------------------------
|   |   | Q |   |   |   | Q |   |
---------------------------------
|   | Q |   |   |   |   |   | Q |
---------------------------------
```

## King

```Python
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
```

```bash
Before Validation
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   | P |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   | P |   | P |   |   |
---------------------------------
|   |   |   | P | K |   |   |   |
---------------------------------
|   |   |   |   | P |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
The move from (4, 4) to (0, 0) is not valid
After Validation
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   | P |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   | P | K | P |   |   |
---------------------------------
|   |   |   | P | K | K |   |   |
---------------------------------
|   |   |   | K | P | K |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
```

## Knight

```Python
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
```

```bash
Before Validation
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   | B |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   | B |   | B |   |   |
---------------------------------
|   |   |   | B |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   | N |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
{(7, 4), (4, 5), (5, 4), (4, 7)}
The move from (6, 6) to (0, 0) is not valid
After Validation
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   | B |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   |   |   |
---------------------------------
|   |   |   | B |   | B |   |   |
---------------------------------
|   |   |   | B |   | N |   | N |
---------------------------------
|   |   |   |   | N |   |   |   |
---------------------------------
|   |   |   |   |   |   | N |   |
---------------------------------
|   |   |   |   | N |   |   |   |
---------------------------------
```
