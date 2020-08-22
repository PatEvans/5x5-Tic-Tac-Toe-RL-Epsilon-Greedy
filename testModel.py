from randomAgent import *
from neuralAgent import *
def randomTest(model,board):
    #test as crosses
    crossWins=0
    noughtWins=0
    draws=0
    originalBoard=copy.deepcopy(board)
    for i in range(0,200):
        print(i)
        while (terminate(board)==-1):
            board=singleNeuralMove(model,board,1)
            if(terminate(board)!=-1):
                break
            board=randMove(board,2)
        
        result=terminate(board)
        board=copy.deepcopy(originalBoard)
        if(result==0):
            crossWins=crossWins+1
        elif(result==1):
            noughtWins=noughtWins+1
        else:
            draws=draws+1

    print("Model won: "+str(crossWins))
    print("Model lost: "+str(noughtWins))
    print("Model drew: "+str(draws))

    #test as noughts
    crossWins=0
    noughtWins=0
    draws=0
    for i in range(0,200):
        print(i)
        while (terminate(board)==-1):
            board=randMove(board,1)

            if(terminate(board)!=-1):
                break
            board=singleNeuralMove(model,board,2)

        result=terminate(board)
        board=copy.deepcopy(originalBoard)
        if(result==0):
            crossWins=crossWins+1
        elif(result==1):
            noughtWins=noughtWins+1
        else:
            draws=draws+1

    print("Model won: "+str(noughtWins))
    print("Model lost: "+str(crossWins))
    print("Model drew: "+str(draws))

    #test as noughts
