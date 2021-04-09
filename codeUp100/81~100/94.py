cnt = int(input())
nums = list(map(int,input().split()))
min = nums[0]

for num in nums :
    if num < min:
        min = num

print(min)

# [기초-리스트] 이상한 출석 번호 부르기3(설명)(py)