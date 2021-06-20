import random
import sys

winComb = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
result = 0
board = {}
for i in range(9):
    board[i] = ' '

def display():
    for i,j in board.items():
        print('    ',j,'    ',end='')
        if i in [2,5]:
            print('')
            print('___________________________________')
            print('')
        elif i not in [2,5,8]:
            print('|',end='')
    print('')

def display_pos():
    for i,j in board.items():
        print('    ',i,'    ',end='')
        if i in [2,5]:
            print('')
            print('___________________________________')
            print('')
        elif i not in [2,5,8]:
            print('|',end='')
    print('')

def any1won():
    for i in winComb:
        if board[i[0]] == board[i[1]] == board[i[2]] and not board[i[0]] == " ":
            if(board[i[0]] == "X"):
                return 1
            elif(board[i[0]] == "O"):
                return 2
    return 0

def userInput():
    u = 1
    while True:
        try:
            u = int(input("Enter position [0-8] :"))
            if validMove(u):
                break
        except:
            continue
    board[u] = "X"

def compInput():
    c = None
    while True:
        c = random.randint(0,9)
        if validMove(c):
            break
    board[c] = "O"

def validMove(input):
    if(board[input] != " "):
        return 0
    return 1

def main():
    global result
    display_pos()
    print("")
    while True:
        print('Computer = O and You = X')
        print("")
        userInput()
        print("")
        result = any1won()
        if(result != 0):
            break
        compInput()
        display()
        print("")
        result = any1won()
        if(result != 0):
            break
    print("")
    display()
    print("")
    print('You Won' if result == 1 else 'You Lose')

if __name__ == "__main__":
    main()
