n,m = map(int,input().split())

datas = []

for _ in range(n):
    data = list(map(int,input().split()))
    minData = min(data)
    datas.append(minData)

print(max(datas))
