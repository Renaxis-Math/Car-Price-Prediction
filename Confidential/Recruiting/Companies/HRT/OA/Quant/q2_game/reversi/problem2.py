def initialize_board(n):
    # Initialize an empty n x n board
    return [['.' for _ in range(n)] for _ in range(n)]

def flip_pieces(board, player, x, y):
    # Helper function to flip pieces in all directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        while 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != '.':
            if board[nx][ny] == player:
                while (nx, ny) != (x, y):
                    board[nx][ny] = player
                    nx, ny = nx - dx, ny - dy
                break
            nx, ny = nx + dx, ny + dy

def play_moves(n, moves):
    board = initialize_board(n)
    for move in moves:
        player, x, y = move.split()
        x, y = int(x), int(y)
        board[x][y] = player
        flip_pieces(board, player, x, y)
    return board

def count_pieces(board):
    black_count = sum(row.count('B') for row in board)
    white_count = sum(row.count('W') for row in board)
    return black_count, white_count

def solution(n, moves):
    final_board = play_moves(n, moves)
    black_pieces, white_pieces = count_pieces(final_board)
    return f"{black_pieces} {white_pieces}"