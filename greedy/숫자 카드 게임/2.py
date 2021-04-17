n,m = map(int,input().split())

result = 0

for _ in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value)

print(result)

# max(a,b) , min(a,b) 를 쓰면 a,b를 비교 할 수 있다.
# 변수 이름 min_value 참고
