## 큰 수의 법칙

n,m,k = map(int,input().split())
arr = list(map(int,input().split()))

maxNum = max(arr)
print(maxNum)

arr.remove(maxNum)
secondMaxNum = max(arr)
print(secondMaxNum)

sum = 0
for i in range(m):
    if i%k == 0 and i != 0:
        sum += secondMaxNum
    else :
        sum += maxNum

print(sum)

## 첫번째로 생각했던 풀이
