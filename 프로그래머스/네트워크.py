from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0

    for com in range(n):
        if visited[com] == False:
            answer += 1

            queue = deque()
            queue.append(com)
            while queue:
                com = queue.popleft()
                visited[com] = True

                for connect in range(n):
                    if computers[com][connect] == 1 and connect != com:
                        if visited[connect] == False:
                            queue.append(connect)
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, computers))