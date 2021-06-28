def solution(X, A):
    check = [0] * X
    check_sum = 0
    answer = -1

    for i in range(len(A)):
        if check[A[i] - 1] == 0:
            check[A[i] - 1] = 1
            check_sum += 1

            if check_sum == X:
                answer = i
                break
    return answer
