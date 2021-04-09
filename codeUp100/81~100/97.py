h,w = map(int,input().split())
board = [ [0 for _ in range(w)] for _ in range(h)]

cnt = int(input())

for _ in range(cnt):
    l,d,x,y = map(int,input().split())

    if d == 0 :
        for i in range(l):
            board[x-1][y+i-1] = 1
    elif d == 1 :
        for i in range(l):
            board[x+i-1][y-1] = 1
    
for i in range(h) :                                
    for j in range(w) :
        print(board[i][j], end=" ")
    print("")


# [기초-리스트] 설탕과자 뽑기(py)