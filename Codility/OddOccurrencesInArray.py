from collections import Counter

def solution(A):
    count_list = Counter(A)

    for i in count_list:
        if count_list[i] % 2 == 1:
            answer = i
            break
    return answer