n,m,k = map(int, input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

sum = 0
for i in range(m):
    if i%k == 0 and i != 0:
        sum += second
    else :
        sum += first

print(sum)

# 가장 큰 수, 두번째로 큰 수를 찾을때 sort 함수를 통해 정렬을 시켜준 후 인덱스로 편하게 뽑아옴
