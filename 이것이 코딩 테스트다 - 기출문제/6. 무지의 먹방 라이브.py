# https://programmers.co.kr/learn/courses/30/lessons/42891 에서 실행
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 시간이 적은 음식부터 빼기 위해 우선순위 큐 사용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식 개수

    # sum_value + ((현재의 음식 시간 - 이전 음식 시간) * 남은 음식 개수) 와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1  # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1])  # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]

# 시간초과 오답

# def solution(food_times, k):
#     answer = 0
#
#     i = -1
#     length = len(food_times)
#     second = 0
#
#     while True:
#         i += 1
#         if k == second:
#             if food_times[i % 3] == 0:
#                 answer = -1
#             else:
#                 answer = (i % 3) + 1
#             #           print("f", food_times[i % 3])
#             break
#
#         if food_times[i % 3] == 0:
#             continue
#
#         food_times[i % 3] -= 1
#         #       print(food_times[i % 3])
#         second += 1
#     #       print("second", second)
#
#     return answer