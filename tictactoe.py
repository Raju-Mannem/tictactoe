#tic_tac_toe python implementation.
def print_board(board):
    print("+---+---+---+")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("+---+---+---+")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("+---+---+---+")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("+---+---+---+")

def check_win(board):
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True

    return False

def check_tie(board):
    return not any(c == ' ' for c in board)

def get_move(board, player):
    while True:
        move = input("Player " + player + ", enter a position (1-9): ")
        try:
            move = int(move) - 1
            if move >= 0 and move < 9 and board[move] == ' ':
                return move
            else:
                print("Invalid move!")
        except ValueError:
            print("Invalid input!")

def tic_tac_toe():
    board = [' '] * 9
    players = ['X', 'O']
    current_player = players[0]

    while True:
        print_board(board)
        move = get_move(board, current_player)
        board[move] = current_player

        if check_win(board):
            print_board(board)
            print("Player " + current_player + " wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("Tie game!")
            break

        current_player = players[(players.index(current_player) + 1) % 2]

tic_tac_toe()


#In the above code, the print_board function prints the current state of the board, the check_win function checks if a player has won the game, the check_tie function checks if the game has ended in a tie, the get_move function prompts the player for their move and returns it if it's valid, and the tic_tac_toe function implements the main game loop.

#To play the game, simply call the tic_tac_toe function. The game will prompt the players for their moves and print the current state of the board after each move. Once the game is over (either because a player has won or the game has ended in a tie), the final state of the board and the result of the game will be printed.
