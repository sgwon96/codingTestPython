# 모험가길드
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성
# 최대 몇개의 모험가 그룹

# 입력
n = int(input())
data = list(map(int,input().split()))

# 정렬 시키고 적은 숫자부터 그룹 만들기
data.sort()

# 리스트에서 한명씩 뽑아서 그룹 숫자 정하기
max_count = 0
count = 0   # 그룹안 사람숫자
result = 0  # 전체 그룹 개수    

for person in data :
    count += 1
    if  count >= person :
        result += 1
        count = 0

print(result)

