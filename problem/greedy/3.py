# 문자열 뒤집기
# 연속된 하나 이상의 숫자를 모두 뒤집어 같은 숫자로 만들기
# 핵심은 0,1 혹은 1,0 이렇게 바뀌는게 얼마나 나오는지

# 입력받기
data = list(map(int,input()))


count = 0

for i in range(1,len(data)):
    prev = data[i-1]
    now = data[i]
    if prev != now :            # 숫자가 바뀔경우 count + 1
        count += 1

print(count//2)

