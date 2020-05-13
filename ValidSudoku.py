# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following
# rules:
#
#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
# Example 1:
# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
#
# Example 2:
# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being
#     modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
# Note:
#
#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.
#     The given board contain only digits 1-9 and the character '.'.
#     The given board size is always 9x9.


for i in range(9):
    for j in range(9):
        print(f'{i, j}', end=' ')
        if j != 0 and j % 8 == 0:
            print('')


# print('')
# for i in range(9):
#     for j in range(9):
#         crow = ((i // 3) * 3) + (j // 3)
#         ccol = ((i % 3) * 3) + (j % 3)
#         print(f'{crow, ccol}', end=' ')
#         if j != 0 and j % 8 == 0:
#             print('')


def valid_sudoku(board):
    row_set = set()
    col_set = set()
    cube_set = set()
    for i in range(9):
        row_set.clear()
        col_set.clear()
        cube_set.clear()
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] in row_set:
                    print(f'invalid value {board[i][j]} at {i}, {j}')
                    return False
                else:
                    row_set.add(board[i][j])

            if board[j][i] != '.':
                if board[j][i] in col_set:
                    print(f'invalid value {board[j][i]} at {j}, {i}')
                    return False
                else:
                    col_set.add(board[j][i])

            cube_row = ((i // 3) * 3) + (j // 3)
            cube_col = ((i % 3) * 3) + (j % 3)
            if board[cube_row][cube_col] != '.':
                if board[cube_row][cube_col] in cube_set:
                    print(f'invalid value {board[cube_row][cube_col]} at {cube_row}, {cube_col}')
                    return False
                else:
                    cube_set.add(board[cube_row][cube_col])
    return True


# def valid_sudoku(board):
#     row_set = set()
#     col_set = set()
#     cube_set = set()
#     for i in range(9):
#         row_set.clear()
#         col_set.clear()
#         cube_set.clear()
#         for j in range(9):
#             if board[i][j] in row_set:
#                 print(f'invalid value {board[i][j]} at {i}, {j}')
#                 return False
#             else:
#                 row_set.add(board[i][j])
#
#             if board[j][i] in col_set:
#                 print(f'invalid value {board[j][i]} at {j}, {i}')
#                 return False
#             else:
#                 col_set.add(board[j][i])
#
#             cube_row = ((i // 3) * 3) + (j // 3)
#             cube_col = ((i % 3) * 3) + (j % 3)
#             if board[cube_row][cube_col] in cube_set:
#                 print(f'invalid value {board[cube_row][cube_col]} at {cube_row}, {cube_col}')
#                 return False
#             else:
#                 cube_set.add(board[cube_row][cube_col])
#     return True


def valid_sudoku2(board):
    row_set = set()
    col_set = set()
    cube_set = set()
    cube_start = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

    for i, j in cube_start:
        cube_set.clear()
        for k in range(i, i + 3):
            for m in range(j, j + 3):
                if board[k][m] in cube_set:
                    print(f'invalid value {board[k][m]} at {k}, {m}')
                    return False
                else:
                    cube_set.add(board[k][m])

    for i in range(9):
        row_set.clear()
        col_set.clear()
        for j in range(9):
            if board[i][j] in row_set:
                print(f'invalid value {board[i][j]} at {i}, {j}')
                return False
            else:
                row_set.add(board[i][j])

            if board[j][i] in col_set:
                print(f'invalid value {board[j][i]} at {j}, {i}')
                return False
            else:
                col_set.add(board[j][i])
    return True


# board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
#          [6, 7, 2, 1, 9, 5, 3, 4, 8],
#          [1, 9, 8, 3, 4, 2, 5, 6, 7],
#          [8, 5, 9, 7, 6, 1, 4, 2, 3],
#          [4, 2, 6, 8, 5, 3, 7, 9, 1],
#          [7, 1, 3, 9, 2, 4, 8, 5, 6],
#          [9, 6, 1, 5, 3, 7, 2, 8, 4],
#          [2, 8, 7, 4, 1, 9, 6, 3, 5],
#          [3, 4, 5, 2, 8, 6, 1, 7, 9]]

assert valid_sudoku([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 4, 5, 2, 8, 6, 1, 7, 9]]) is True

assert valid_sudoku([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 4, 5, 2, 8, 6, 1, 7, 1]]) is False

assert valid_sudoku([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                     [4, 2, 6, 8, 5, 2, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 4, 5, 2, 8, 6, 1, 7, 9]]) is False

assert valid_sudoku2([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 2, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]) is False

# board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
#          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#          [".", "9", "8", ".", ".", ".", ".", "6", "."],
#          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#          [".", "6", ".", ".", ".", ".", "2", "8", "."],
#          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(valid_sudoku(board))
