# N의 범위가 100 이하로 매우 적기 때문에 플로이드 워셜 알고리즘 활용

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 전체 회사의 개수 N과 경로의 개수 M 입력
n,m = map(int,input().split())

# 노드와 간선을 입력할 그래프 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1,n+1):
    for j in range(1, n+1):
        if i == j :
            graph[i][j] = 0

# 연결된 두 회사 M개 입력 받기
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# X와 k 입력받기
x, k = map(int,input().split())

# 플로이드 워셜 알고리즘 수행
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else :
    print(distance)
            

