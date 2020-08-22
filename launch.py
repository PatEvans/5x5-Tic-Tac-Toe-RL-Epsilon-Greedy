from epsilonTrain import *
from neuralModel import *
from testModel import *
from neuralAgent import *
import copy
n = 5

neural=neuralModel()
neural.createModel()
option=input("Do you want to train a model or load a model? ( t / l )")

if(option=="t"):
    #produce training data via random policy
    count=0
    increment=0
    for i in range(0,40):
        board = [[0 for i in range(n+1)] for j in range(n)]
        board[0][n]=1
        trainingData=epsilonData(board,neural.model,increment)
        count=count+1
        if(count==10):
            count=0
            increment=increment+5
        #and train neural model using the data produced
        neural.trainModel(trainingData)
    neural.model.save('EpsilonModel.h5')

else:
    from tensorflow import keras
    neural.model=keras.models.load_model('EpsilonModel.h5')

    print("Loaded!")
#test the model
board = [[0 for i in range(n+1)] for j in range(n)]
board[0][n]=1
randomTest(neural.model,board)
