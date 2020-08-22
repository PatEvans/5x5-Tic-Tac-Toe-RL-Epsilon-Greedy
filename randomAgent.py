from random import *
def randMove(board,player):
    firstRand=randint(0, len(board)-1)
    secondRand=randint(0,len(board)-1)
    while True:
        if(board[firstRand][secondRand]==0):
            board[firstRand][secondRand]=player
            break
        firstRand=randint(0, len(board)-1)
        secondRand=randint(0,len(board)-1)
    return board

def parallelRandMove(boards,player):
    for board in boards:
        firstRand=randint(0, len(board)-1)
        secondRand=randint(0,len(board)-1)
        while True:
            if(board[firstRand][secondRand]==0):
                board[firstRand][secondRand]=player
                break
            firstRand=randint(0, len(board)-1)
            secondRand=randint(0,len(board)-1)
    return boards
