def solution(S, P, Q):
    answer = []
    n = len(P)

    for i in range(n):
        if 'A' in S[P[i]:Q[i] + 1]:
            answer.append(1)
        elif 'C' in S[P[i]:Q[i] + 1]:
            answer.append(2)
        elif 'G' in S[P[i]:Q[i] + 1]:
            answer.append(3)
        else:
            answer.append(4)

    return answer