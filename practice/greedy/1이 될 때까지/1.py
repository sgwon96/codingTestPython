n,k = map(int, input().split())
count = 0

while n != 1 :
    if n%k == 0 :
        n = n/k
        count += 1
        continue
    else :
        n = n-1
        conunt += 1

print(count)    