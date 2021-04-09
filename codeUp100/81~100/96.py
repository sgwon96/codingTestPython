d = []
for i in range(19):                                 # 입력
    line = list(map(int,input().split()))
    d.append(line)

cnt = int(input())

for _ in range(cnt):
    a,b = map(int,input().split())
    for i in range(19) :                            # 가로줄 뒤집기
        d[a-1][i] = 0 if d[a-1][i] == 1 else 1
    for j in range(19) :                            # 세로줄 뒤집기
        d[j][b-1] = 0 if d[j][b-1] == 1 else 1

for i in range(19) :                                # 출력
    for j in range(19) :
        print(d[i][j], end=" ")
    print("")

# 6096 : [기초-리스트] 바둑알 십자 뒤집기(py) 

