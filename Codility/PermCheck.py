def solution(A):
    A.sort()
    answer = 0
    target = 1

    for i in A:
        if i != target:
            break
        target += 1
    if target - 1 == len(A):
        answer = 1

    return answer
