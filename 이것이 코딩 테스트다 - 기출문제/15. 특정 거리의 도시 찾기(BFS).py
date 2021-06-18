# BFS 사용 (거리가 1일때 BFS로 최단경로 탐색 가능)

from collections import deque

n, m, k, x = map(int, input().split())

# a, b를 x, y로 했을 때 마지막 값의 x가 저장되어 원하는 결과가 안나왔음
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시 까지의 거리는 0으로 설정

queue = deque([x]) # 시작 노드 큐 삽입

# 큐가 빌 때까지 반복
while queue:
    now = queue.popleft() # 큐에서 하나의 원소를 뽑아 출력
    print(now)
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            queue.append(next_node)
    print(queue)
print(distance)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)