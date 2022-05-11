def display_board(board):
    print(" _________")
    print("|" + board[0] + " | " + board[1] + " | " + board[2] + "| " )
    print(" _________")
    print("|" + board[3] + " | " + board[4] + " | " + board[5] + "| " )
    print(" _________")
    print("|" + board[6] + " | " + board[7] + " | " + board[8] + "| " )
    print(" _________")

    
def win_check(board, mark):
    # Mark kara lini kam X kam O
    
    if board[0] == board[1] == board[2] == mark:
        return True
    if board[3] == board[4] == board[5] == mark:
        return True
    if board[6] == board[7] == board[8] == mark:
        return True
    if board[0] == board[3] == board[6] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[0] == board[4] == board[8] == mark:
        return True
    if board[2] == board[4] == board[6] == mark:
        return True
    return False

# stugumem ardyoq tvyal dirqum unem X kam O
def draw_check(board):
    
    for i in board:
        if i != "X" and i != "O": # Check if digit
            return False 
        
    return True 

def place_check(board, index):
    # Stugum enq texy azat e te voch
    
    if board[index] == "X" or board[index] == "O":
        return False
    else:
        return True

board_current = ["1","2","3",
                "4","5","6",
                "7","8","9"]

player1_name = input("Player 1 name : ")
player2_name = input("Player 2 name : ")

players = {-1: player1_name, 
           1: player2_name}

markers = {-1: "X", 
           1: "O"}

i = -1 #Xaxacoxi cucichy

while True:
    
    current_player = players[i] 
    display_board(board_current)
    print("\n")
    # Xaxacoxi qayly
    try:
        current_move = int(input(current_player + " moves : ")) - 1
    except:
        print("False move!! Game over! Please enter a digit from 1 to 9")
        break;
    
    # Stugumenq qaylery range um en te voch
    if (current_move > 8) or (current_move < 0):
        
        print("False move!! Game over! Please enter a digit from 1 to 9")
        break;
        
    # Stugumenq ardyoq tex unenq Xi kam Oi hamar
    while not place_check(board_current, current_move): # ete tex chunenq
        
        print("The space is not empty! Try other space")
        current_move = int(input(current_player + " moves : ")) - 1
    
    board_current[current_move] = markers[i]
    
    # Stugumenq haxtoxin
    if win_check(board_current, markers[i]):
        
        display_board(board_current)
        print(current_player + " wins!! Shnorhavor cavd tanem!")
        break;
    
    # stugumenq gravvac texery
    if draw_check(board_current):
        
        display_board(board_current)
        print("DRAW! Game over!")
        break;

    i *= -1 # Xaxacoxneri herdakanutyuny
        
    