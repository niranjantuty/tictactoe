
# board
# switch players
    # change board value
    # check win
        # check rows
        # check columns
        # check diagonals
    # check tie
# end game

board = [
        '-', '-', '-',
        '-', '-', '-',
        '-', '-', '-'
    ]
game = True
def display_board():
    for i in range(1, 10):
        if i%3 != 0:
            print(" " + board[i-1] , end=" |")
        elif i%3 ==0:
            print(" " + board[i-1], end="")
            print()
    print("------------")
    for i in range(1,10):
        if i%3 != 0:
            print(" " + str(i), end = " |")
        elif i%3 == 0:
            print(" " + str(i), end = "")
            print()

def switch_players(current_player):
    if current_player == 1:
        current_player=2
        return current_player
    current_player=1
    return current_player
    
def play_on_board(current_player):
    print(f"Player {current_player}, your turn")
    while True:
        pos = input("Enter 1-9: ")
        try:
            pos = int(pos)
        except:
            print("Invalid input")
            continue
        if not 1<=pos<=9:
            continue
        if board[pos-1] == '-':
            if current_player == 1:
                board[pos-1] = 'X'
            elif current_player == 2:
                board[pos-1] = 'Y'
            break
        else:
            print("It's occupied")

def check_win(current_player):
    check_rows()
    check_columns()
    check_diagonals()
    if not game:
        print(f"Player {current_player} won.")


def check_rows():
    global game
    if board[0] == board[1] == board[2] != '-':
        game=False
    elif board[3] == board[4] == board[5] != '-':
        game = False
    elif board[6] == board[7] == board[8] != '-':
        game = False

def check_columns():
    global game
    if board[0] == board[3] == board[6] != '-':
        game=False
    elif board[1] == board[4] == board[7] != '-':
        game = False
    elif board[2] == board[5] == board[8] != '-':
        game = False

def check_diagonals():
    global game
    if board[0] == board[4] == board[8] != '-':
        game=False
    elif board[2] == board[4] == board[6] != '-':
        game = False  

def check_tie():
    global game
    if '-' not in board:
        game = False
        print("Tie game")

def play_game():
    global game
    current_player = 1
    display_board()
    while game:
        play_on_board(current_player)
        display_board()
        check_win(current_player)
        check_tie()
        current_player = switch_players(current_player)
        
      
if __name__ == '__main__':
    play_game()
