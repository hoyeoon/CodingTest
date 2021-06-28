def solution(A):
    n = len(A)
    if n == 1:
        if A[0] == 1:
            return 2
        else:
            return 1

    answer = 0
    A.sort()

    for i in range(n):
        if A[i] != i + 1:
            answer = i + 1
            break
    if answer == 0:
        answer = n + 1
    return answer
