def solution(A, B, K):
    start = end = 0
    for i in range(A, B + 1):
        if i % K == 0:
            start = i
            break
    for i in range(B, A - 1, -1):
        if i % K == 0:
            end = i
            break

    if A == B:
        if A % K == 0:
            answer = 1
        else:
            answer = 0
    else:
        answer = (end - start) // K + 1

    return answer