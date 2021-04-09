d = [[0 for j in range(19)] for i in range(19)] 
cnt = int(input())

for _ in range(cnt):
    x,y = map(int,input().split())
    d[y-1][x-1] = 1

for i in range(19) :
    for j in range(19) :
        print(d[j][i], end=" ")
    print("")

# [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)