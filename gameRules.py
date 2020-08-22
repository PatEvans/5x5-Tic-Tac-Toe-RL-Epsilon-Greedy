import copy

#Function terminate takes in board as list
#returns 1 if X has won
#returns 2 if O has won
#returns 3 if draw
#returns 0 if no result
def terminate(board):
    #check horizontal
    for x in board:
        horizontal=""
        for y in range(0,len(board)):
            horizontal+=str(x[y])
        if("1111" in horizontal):
            return 0
        elif("2222" in horizontal):
            return 1

    #check vertical
    for i in range(0,len(board)):
        vertical=""
        for j in range(0,len(board)):
            vertical+=str(board[j][i])
        if("1111" in vertical):
            return 0
        elif("2222" in vertical):
            return 1

    #check one diagonal
    for i in range(0,2*len(board)-1):
        j=0
        diagonal=""
        while True:
            if(i-j <len(board) and j<len(board)):
                diagonal+=str(board[j][i-j])


            if(j==i or (i-j)<0):
                break
            j=j+1
        if("1111" in diagonal):
            return 0
        elif("2222" in diagonal):
            return 1

     #check other diagonal
    for i in range(0,2*len(board)-1):
        j=0
        otherDiagonal=""
        while True:
            if(i-j <len(board) and j<len(board)):
                otherDiagonal+=str(board[j][(len(board)-1)-(i-j)])

            if(j==i or (i-j)<0):
                break
            j=j+1
        if("1111" in otherDiagonal):
            return 0
        elif("2222" in otherDiagonal):
            return 1

    #check if full
    notFull=False
    for x in board:
        horizontal=""
        for y in range(0,len(board)):
            horizontal+=str(x[y])
        if("0" in horizontal):
            notFull=True
    if(notFull==False):
        return 2
    return -1

#makeMove takess in x and y coords , board as list and player
#list is updated with new move made
def makeMove(xMove,yMove,board,player):
    if(board[xMove][yMove]!=0):
        return False
    else:
        if(player==True):
            board[xMove][yMove]=1
        else:
            board[xMove][yMove]=2

#passes in a board and player and returns a list of all possible
#moves that can be made y this player on this board
def getChildren(board,player):
    children=[]
    for i in range(0,len(board)):
            for j in range(0,len(board)):
             if(board[i][j]==0):
                board[i][j]=player
                newboard=copy.deepcopy(board)
                board[i][j]=0
                children.append(newboard)
    return children

#printBoard outputs text representation of board to standard output
def printBoard(board):
    for x in board:
        for y in x:
            if(y==1):
                print ("X", " ", end="")
            elif(y==2):
                print("O", " ", end="")
            else:
               print("_", " ", end="")
        print("")
