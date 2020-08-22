from gameRules import *
from random import *
from randomAgent import *
from neuralAgent import *
import copy

def epsilonData(board,model,epsilon):
    originalBoard=copy.deepcopy(board)
    games=epsilonGames(board,10000,epsilon,model)
    board=copy.deepcopy(originalBoard)
    return games

def epsilonGames(board,numGames,epsilon,model):
    games=[]
    boards=[]
    returnValues=[]
    player=1
    crossWins=0
    noughtWins=0
    draws=0
    moveNum=0
    for i in range(numGames):
        boards.append(copy.deepcopy(board))
        games.append([copy.deepcopy(boards[i])])

    while(len(boards)!=0):
        moveNum=moveNum+1
        #for each board, we have a chance for a nn move rather than
        #random. These nn moves and rand boards are then separated

        #split into two separate list via random method
        nnBoards=[]
        randBoards=[]
        for i in range(0,len(boards)):
                rand=randint(0, epsilon)
                if(rand==epsilon or moveNum<=2):
                    randBoards.append(boards[i])
                else:
                    nnBoards.append(boards[i])

        if(len(nnBoards)!=0):
            nnBoards=parallelNeuralMove(model,nnBoards,player)
        if(len(randBoards)!=0):
            randBoards=parallelRandMove(randBoards,player)

        if(player==1):
            player=2
        else:
            player=1

        #remove finished games
        toPop=[]
        for i in range(0,len(boards)):
            boards[i][0][5]=player
            games[i].append(copy.deepcopy(boards[i]))
            if(terminate(boards[i])!=-1):
                toPop.append(i)

        for i in range(len(toPop)-1,-1,-1):
            game=games.pop(toPop[i])
            board=boards.pop(toPop[i])
            result=terminate(board)
            if(result==0):
                crossWins=crossWins+1
            elif(result==1):
                noughtWins=noughtWins+1
            else:
                draws=draws+1

            returnValues.append([game,result])

    print("Cross:"+str(crossWins))
    print("Noughts:"+str(noughtWins))
    print("Draws:"+str(draws))
    return returnValues
