from time import sleep
from random import randint


print("Game is begining")
sleep(2)

dict = {}
dict[0] = [8, 2, 1, 6, 4, 3]
dict[1] = [4, 8, 6, 2, 0, 5]
dict[2] = [6, 0, 1, 8, 4, 7]
dict[3] = [4, 2, 8, 0, 6, 1]
dict[4] = [5, 0, 8, 2, 6, 1]
dict[5] = [4, 0, 6, 2, 1, 8]
dict[6] = [2, 0, 3, 8, 4, 5]
dict[7] = [4, 0, 2, 6, 3, 8]
dict[8] = [0, 2, 7, 6, 4, 1]

x_1 = randint(0, 8)

def tic_tac_toe(state, a):
    ls = ["*","*","*","*","*","*","*","*","*"]
    ls[a] = "X"
    print("___________________")
    print("| ",ls[0]," | ",ls[1]," | ",ls[2]," | ")
    print("___________________")
    print("| ",ls[3]," | ",ls[4]," | ",ls[5]," | ")
    print("___________________")
    print("| ",ls[6]," | ",ls[7]," | ",ls[8]," | ")
    print("___________________")
    sleep(2)
    n = -1
    for i in range(len(state)):
        if n > 0:
            ls[state[i]] = "X"
        else:
            ls[state[i]] = "O"
        n *= -1    
        print("___________________")
        print("| ",ls[0]," | ",ls[1]," | ",ls[2]," | ")
        print("___________________")
        print("| ",ls[3]," | ",ls[4]," | ",ls[5]," | ")
        print("___________________")
        print("| ",ls[6]," | ",ls[7]," | ",ls[8]," | ")
        print("____________________")
        sleep(2)
    print("Player 1 wins")
        
tic_tac_toe(dict[x_1],x_1)        
        