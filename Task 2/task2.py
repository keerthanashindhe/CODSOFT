import math

def print_board(board):
    for i in range(3):
        print(board[i*3:(i+1)*3])
    print()

def is_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]             # diagonals
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

def is_draw(board):
    return all(pos in ['X', 'O'] for pos in board)

def get_empty_positions(board):
    return [i for i, pos in enumerate(board) if pos not in ['X', 'O']]
def minimax(board, depth, is_maximizing):
    if is_winner(board, 'X'):
        return -10 + depth  # Prefer faster win for 'O'
    if is_winner(board, 'O'):
        return 10 - depth   # Prefer faster win for 'O'
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_empty_positions(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = move
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_empty_positions(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = move
            best_score = min(score, best_score)
        return best_score
def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_empty_positions(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = move
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
def play_game():
    board = [i for i in range(9)]
    print_board(board)

    while True:
        # Human move
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] in ['X', 'O']:
            print("Invalid move! Try again.")
            continue
        board[human_move] = 'X'
        print_board(board)

        if is_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI move
        print("AI's turn...")
        ai_move = find_best_move(board)
        board[ai_move] = 'O'
        print_board(board)

        if is_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a draw!")
            break

play_game()
