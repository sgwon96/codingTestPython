cnt = int(input())
nums = list(map(int,input().split()))
d = [ 0 for _ in range(23)]

for num in nums:
    d[num-1] = d[num-1] + 1

for answer in d :
    print(answer,end=" ")

# [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)