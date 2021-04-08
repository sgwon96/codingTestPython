n = int(input())

for i in range(1,n+1) :
    if (i%10)%3 == 0 and i%10 != 0 :
        print("X", end=' ')
        continue
    print(i, end=' ')



# 6082 : [기초-종합] 3 6 9 게임의 왕이 되자(설명)