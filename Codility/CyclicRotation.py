def solution(A, K):
    answer = []
    if not A:
        return answer

    N = len(A)
    K = K % N

    for i in range(N - K, N):
        answer.append(A[i])
    for i in range(0, N - K):
        answer.append(A[i])

    return answer