n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans :
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny <1 or nx > n or ny > n:
        continue
    x,y = nx,ny

print(x,y)

# 상하좌우
# 좌표를 이동할때는 dx, dy, move_types 세가지 리스트를 만든 후 move_types 확인하고 x,y 에 dx,dy 더하는 식으로 이동시켜준다.

