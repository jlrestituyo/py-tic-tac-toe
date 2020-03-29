from random import randrange

board = {1:" ",2:" ",3:" ",4:" ",5:"X",6:" ",7:" ",8:" ",9:" "}
available_plays = 8

def DisplayBoard(board_values):
    board= ("+" + "-" * 9) * 3 + "+\n" \
    ""+ ("|         " * 4 ) + "\n" \
    "|    "+  board_values[1]  +"    "   +   "|    "+  board_values[2]   +"    " + "|    "+  board_values[3]   +"    |\n" \
    ""+ ("|         " * 4 ) +"\n" \
    ""+ ("+" + "-" * 9) * 3 + "+\n" \
    ""+ ("|         " * 4 ) + "\n" \
    "|    "+  board_values[4]  +"    "   +   "|    "+  board_values[5]   +"    " + "|    "+  board_values[6]   +"    |\n" \
    ""+ ("|         " * 4 ) +"\n" \
    ""+ ("+" + "-" * 9) * 3 + "+\n" \
    ""+ ("|         " * 4 ) + "\n" \
    "|    "+  board_values[7]  +"    "   +   "|    "+  board_values[8]   +"    " + "|    "+  board_values[9]   +"    |\n" \
    ""+ ("|         " * 4 ) +"\n" \
    ""+ ("+" + "-" * 9) * 3 + "+\n"
    
    print(board)


def player_move(board):
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
    move = int(input("Enter your move: "))
    while (board[move] in ("X","O") ):
       move = int(input("Move not allowed!, re-enter: "))
    else:
        board[move] = "O"
        global available_plays 
        available_plays = available_plays -1


def computer_move(board):
    move = int(randrange(1,10))
    while (board[move] in ("X","O") ):
       move = int(randrange(1,10))
    else:
        board[move] = "X"
        global available_plays 
        available_plays -= 1




def vicoty_found(board, sign):
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
    if(sign == board[1] and sign == board[2] and sign == board[3]):
        return True
    elif (sign == board[1] and sign == board[5]  and sign == board[9]):
        return True
    elif (sign == board[1] and sign == board[4]  and sign == board[7]):
        return True
    elif (sign == board[2] and sign == board[5]  and sign == board[8]):
        return True
    elif (sign == board[3] and sign == board[5]  and sign == board[7]):
        return True
    elif (sign == board[3] and sign == board[6]  and sign == board[9]):
        return True
    elif (sign == board[4] and sign == board[5]  and sign == board[6]):
        return True
    elif (sign == board[7] and sign == board[8]  and sign == board[9]):
        return True
    else:
        return False



def winner(board):
# the function draws the computer's move and updates the board
    winner = False
    if(vicoty_found(board,"X")):
        print("The winer is: Computer")
        winner = True
    elif(vicoty_found(board,"O")):
        print("The winer is: User")
        winner = True
    else:
        if(available_plays == 0):
            print("No winer, it's Draw")

    return winner


DisplayBoard(board)
while(available_plays > 1):
    player_move(board)
    DisplayBoard(board)
    if(winner(board)):
        break

    computer_move(board)
    DisplayBoard(board)
    if(winner(board)):
        break











