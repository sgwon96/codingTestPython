d = []
for i in range(10):                                 # 입력
    line = list(map(int,input().split()))
    d.append(line)


x,y = 1,1
onRoad = True

while onRoad :
    if d[x][y] == 2 :
        onRoad = False
    d[x][y] = 9   
    if d[x][y+1] != 1 :
        y = y + 1
    elif d[x+1][y] != 1 :
        x = x + 1
    else :
        break


for i in range(10) :                                # 출력
    for j in range(10) :
        print(d[i][j], end=" ")
    print("")

# 6098 : [기초-리스트] 성실한 개미(py)