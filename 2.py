# 곱하기 혹은 더하기
# X 혹은 + 를 이용해 가장 큰 수 출력
# 0,1 이면 + 아니면 x



# 입력받기 
data = list(map(int,input()))

# 결과값 선언
result = 1

# data에서 숫자를 하나씩 뽑아 계산
for num in data :
    if num == 0 or num == 1 :
        result += num
    else :
        result *= num


# 결과값 출력
print(result)