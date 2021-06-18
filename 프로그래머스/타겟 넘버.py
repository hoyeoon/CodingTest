from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0, 0))

    while queue:
        sum, idx = queue.popleft()

        if idx < len(numbers):
            queue.append((sum + numbers[idx], idx + 1))
            queue.append((sum - numbers[idx], idx + 1))
        else:
            if sum == target:
                answer += 1

    return answer