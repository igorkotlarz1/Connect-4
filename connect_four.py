import os

def clear_term():
    os.system('cls')

# creating 6 x 7 connect 4 board
board = [['_' for _ in range(7)] for _ in range(6)]

#displaying the board
def display_board(board):

    for i in range(7):
        print(f'  {i+1}', end=' ')
    print()

    for i in range(6):
        print('+---'*7 + '+')
        for j in range(7):
            print(f'| {board[i][j]}', end=' ')
            if j == 6:
                print('|')
    print('+---'*7 + '+')

#inserting an element into a valid spot in the board
def insert(col:int, elem:str):
    os.system('cls')

    if col not in range(1,8):
        raise ValueError(f'Unable to insert an element into column {col} because it is not a valid spot!')
    if elem.upper() not in {'X','O'}:
        raise ValueError(f'{elem} is not a valid element! You can either insert X or O!')
    global board

    if board[0][col-1] not in {'X','O'}:      
        i:int = len(board)-1
        while i >= 0:
            if board[i][col-1] == '_':
                board[i][col-1] = elem
                break
            else:
                i -= 1
        display_board(board)        
    else:
        print(f'Unable to insert an element into column {col} because it is full!')      


insert(2,'d')
