position = input()

x = ord(position[0])      # a=97 h=104
y = int(position[1])
answer = 0


steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]   # 이동 가능한 경우의 수

for step in steps :             # 경우의수를 하나씩 모두 확인
    inBoard = True
    nx = x + step[0]
    ny = y + step[1]

    if nx < 97 or nx > 104:     # x가 범위안에 있는지 확인
        inBoard = False
    if ny < 1 or ny > 8 :       # y가 범위안에 있는지 확인
        inBoard = False
    
    if inBoard :                # x,y가 모두 범위안에 있으면 답을 1 증가    
        answer += 1
    
print(answer)
