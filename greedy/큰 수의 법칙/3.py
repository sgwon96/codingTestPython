n,m,k = map(int, input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count  = (m//(k+1)) * k 
count += m % (k+1)

result = 0
result += first * count         # 가장 큰 수 더하기
result += second * (m-count)      # 두번째로 큰 수 더하기

print(result)

# for 함수를 쓰지않고 수열의 규칙을 파악