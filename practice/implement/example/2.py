h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

# 시각
# 시간, 분 , 초를 문자열로 모두 합친 후 3이 포함되어 있는지 확인 한 후 있으면 count 1 증가