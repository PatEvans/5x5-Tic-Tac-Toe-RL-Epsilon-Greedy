import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from gameRules import *

def calcValue(boards,model):
    tensorBoards=np.array(boards).reshape(-1,30)
    tensorBoards = tf.convert_to_tensor(tensorBoards,dtype=tf.float32)
    prediction=model.predict(tensorBoards,batch_size=256)
    return prediction

def singleNeuralMove(model,board,player):
    children=getChildren(board,player)
    #+ve value for cross win
    #-ve value for noughts win
    if(player==1):
        maxVal=-100000
    else:
        maxVal=100000
    maxIndex=-1
    valArray=calcValue(children,model)
    for j in range(0,len(children)):
        if(player==1):
            current=valArray[j][0]-valArray[j][1]

        elif(player==2):
            current=valArray[j][1]-valArray[j][0]

            if(current>maxVal):
                maxVal=current
                maxIndex=j

    if(maxVal<0):
        maxVal=-100000
        maxIndex=-1
        for j in range(0,len(children)):
            if(player==1):
                current=valArray[j][2]-valArray[j][1]

            elif(player==2):
                current=valArray[j][2]-valArray[j][0]

                if(current>maxVal):
                    maxVal=current
                    maxIndex=j
    board=children[maxIndex]
    #print(board)
    return board


def parallelNeuralMove(model,boards,player):
    totalChildren=[]
    childNum=[]
    for board in boards:
        children=getChildren(board,player)
        childNum.append(len(children))
        for child in children:
            totalChildren.append(child)
    #+ve value for cross win
    #-ve value for noughts win

    valArray=list(calcValue(totalChildren,model))
    bestBoard=[]
    for i in range(len(boards)):
        maxVal=-100000
        maxIndex=-1
        boardList=[totalChildren.pop(0) for idx in range(childNum[i])]
        valList= [valArray.pop(0) for idx in range(childNum[i])]

        for j in range(0,childNum[i]):
            if(player==1):
                current=valList[j][0]-valList[j][1]

            elif(player==2):
               current=valList[j][1]-valList[j][0]

            if(current>maxVal):
                maxVal=current
                maxIndex=j

        if(maxVal<0):
            maxVal=-100000
            maxIndex=-1
            for j in range(0,childNum[i]):
                if(player==1):
                    current=valList[j][2]-valList[j][1]

                elif(player==2):
                    current=valList[j][2]-valList[j][0]

                if(current>maxVal):
                    maxVal=current
                    maxIndex=j

        bestBoard=boardList[maxIndex]
        for x in range(0,len(boards[i])):
            for y in range(0,len(boards[i][x])):
                boards[i][x][y]=bestBoard[x][y]

    return boards
