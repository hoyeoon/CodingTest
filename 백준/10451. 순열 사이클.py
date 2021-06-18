# 입력
# 2
# 8
# 3 2 7 8 1 4 5 6
# 10
# 2 1 3 4 5 6 7 9 10 8

# 출력
# 3
# 7
from collections import deque

t = int(input())
for i in range(t):
    answer = 0
    n = int(input())
    l = list(map(int, input().split()))
    visited = [False] * n

    for node in range(n):
        if visited[node] == False:
            visited[node] = True
            if node == l[node] - 1:
                answer += 1
            else:
                queue = deque()
                queue.append((node, l[node]))  # (node, value)
                while queue:
                    node, next_node = queue.popleft()
                    if visited[next_node - 1] == False:
                        visited[next_node - 1] = True
                        queue.append((next_node - 1, l[next_node - 1]))
                answer += 1
    print(answer)