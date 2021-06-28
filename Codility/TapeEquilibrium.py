def solution(A):
    n = len(A)

    op1 = [A[0]]
    for i in range(1, n - 1):
        op1.append(A[i] + op1[-1])

    op2 = [A[n - 1]]
    for i in range(n - 2, 0, -1):
        op2.append(A[i] + op2[-1])

    answer = []
    for i in range(n - 1):
        answer.append(abs(op1[i] - op2[n - 2 - i]))
    return min(answer)