import numpy as np

def solution(board, moves):

    board = np.transpose(board)

    arr=[]
    answer=0
    for i in moves:
        for j in range(len(board[0])):
            a= board[i-1][j]
            if a != 0:
                board[i-1][j]=0
                arr.append(a)
                break
        if len(arr)>1 and arr[-1] == arr[-2]:
            answer +=1
            del arr[-1], arr[-1]


    return answer*2

print(solution([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], [1,3,2,1,3,4,2,1]))