
def print_board(board):

    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):

    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)


def is_draw(board):
    return all(space != " " for space in board)

def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    print("Welcome to TIC-TAC-TOE!")
    print("This is a two player TIC-TAC-Toe Game!")
    print_board(board)

    while True:
        try:
            move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please choose a number between 1 and 9.")
                continue
            if board[move] != " ":
                print("That space is already taken. Try again.")
                continue

            board[move] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"🎉 Player {current_player} wins!")
                break
            elif is_draw(board):
                print("It's a draw! 🤝")
                break

            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

    print("Game over!")


if __name__ == "__main__":
     tic_tac_toe()