
import random

#creating the board size
board_size=4
#to display the board
def display():
    #we find the largest element for maintaining even spaces
    lar=board[0][0]
    for row in board:
        for element in row:
            if(element>lar):
                lar=element
    #length of largest element
    l=len(str(lar))
    for row in board:
        curr='|'
        for element in row:
            if(element==0):
                curr+=' '*l+'|'
            else:
                curr+=(' '*(l-len(str(element))))+str(element)+'|'
        print(curr)
#merging one row left
def mergeonerowl(row):
    # we move everything to the left
    for j in range(board_size-1):
        for i in range(board_size-1,0,-1):
            #we check if there is empty space and then move
            if row[i-1]==0:
                row[i-1]=row[i]
                row[i]=0
    #merge to the left
    for i in range(board_size-1):
        #check if adjacent values are same
        if(row[i]==row[i+1]):
            row[i]*=2
            row[i+1]=0
    for i in range(board_size-1,0,-1):
        if row[i-1]==0:
            row[i-1]=row[i]
            row[i]=0
    return row
#merging entire board to the left
def mergeleft(currentboard):
    #merge every row in board left
    for i in range(board_size):
        currentboard[i]=mergeonerowl(currentboard[i])
    return currentboard
#reversing the order of one row
def reverse(row):
    #adding reversed elements in new list
    li=[]
    for i in range(board_size-1,-1,-1):
        li.append(row[i])
    return li
#merging the board to right
def mergeright(currentboard):
    for i in range(board_size):
        #reversing the row,merging left,and then reverse back
        currentboard[i]=reverse(currentboard[i])
        currentboard[i]=mergeonerowl(currentboard[i])
        currentboard[i]=reverse(currentboard[i])
    return currentboard
#transpose the board
def transpose(currentboard):
    for j in range(board_size):
        for i in range(j,board_size):
            if i!=j:
                temp=currentboard[i][j]
                currentboard[i][j]=currentboard[j][i]
                currentboard[j][i]=temp
    return currentboard
#below function merges up
def mergeup(currentboard):
    #transpose,merge left,transpose back
    currentboard=transpose(currentboard)
    currentboard=mergeleft(currentboard)
    currentboard=transpose(currentboard)
    return currentboard
#function to merge down
def mergedown(currentboard):
    #transpose,merge right,transpose back
    currentboard=transpose(currentboard)
    currentboard=mergeright(currentboard)
    currentboard=transpose(currentboard)
    return currentboard

    return currentboard
#pick a value for board
def pickvalue():
    if random.randint(1,8)==1:
        return 4
    else:
        return 2
#add value to board
def addvalue():
    row=random.randint(0,board_size-1)
    col=random.randint(0,board_size-1)
    #picking an empty spot
    while not board[row][col]==0:
        row=random.randint(0,board_size-1)
        col=random.randint(0,board_size-1)
    board[row][col]=pickvalue()
#if he has won
def won():
    for row in board:
        if 2048 in row:
            return True
    return False
#if he has lost
def lost():
    #two copies of boards
    t1=board.copy()
    t2=board.copy()
    #testing all possible moves
    t1=mergedown(t1)
    if t1==t2:
        t1=mergeup(t1)
        if t1==t2:
            t1=mergeright(t1)
            if t1==t2:
                t1=mergeleft(t1)
                if t1==t2:
                    return True
    return False
#create a blank board
board=[]
for i in range(board_size):
    row=[]
    for j in range(board_size):
        row.append(0)
    board.append(row)
#fill two spots to start the game
num=2
while num>0:
    row=random.randint(0,board_size-1)
    col=random.randint(0,board_size-1)
    if board[row][col]==0:
        board[row][col]=pickvalue()
        num-=1
print('welcome to 2048')
print('Enter 1,2,3,4 to merge left,right,up,down')
display()
chances=False
#repeat until there are no chances
while not chances:
    move=input('Enter: ')
    #assuming it is valid input
    valid=True
    temp=board.copy()
    #create a copy of board
    if move=='1':
        mergeleft(board)
    elif move=='2':
        mergeright(board)
    elif move=='3':
        mergeup(board)
    elif move=='4':
        mergedown(board)
    else:
        valid=False
    if not valid:
        print('invalid input')
    else:
        #check if move was successfull
        if temp==board:
            print('try different direction')
        else:
            #if he has won
            if won():
                display()
                print('You Won')
                chances=True
            else:
                addvalue()
                display()
                #check if they lost
                if lost():
                    print('no more chances')
                    chances=True


