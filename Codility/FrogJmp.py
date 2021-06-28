def solution(X, Y, D):
    diff = Y - X
    answer = diff // D
    if diff % D > 0:
        answer += 1
    return answer