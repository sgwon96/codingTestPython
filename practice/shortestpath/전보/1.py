# N의 개수가 30000개 까지 가능하기 떄문에 다익스트라 알고리즘 활용

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 도시의 개수(노드) N, 통로의 개수(간선) M, 출발지(시작 노드) C 입력받기
n,m,start = map(int,input().split())

# 최단거리를 저장할 리스트 초기화
distance = [INF] * (n+1)

# 도시간 통로와 시간을 기록하기 위한 그래프 초기화
graph = [[] for _ in range(n+1)]

# 모든 간선 정보를 입력 받기
for _ in range(m):
    x,y,z = map(int,input().split()) # X에서 Y로 갈때 시간 Z가 걸린다.
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않으면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 이미 방문한 노드일 경우 계산 X
        if distance[now] < dist :
            continue
        # 현재 노드와 인접한 다른 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            if  cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,now))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드를 제외하고 출력
print(count-1, max_distance)
