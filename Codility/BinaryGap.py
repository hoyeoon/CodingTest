def solution(N):
    answer = 0
    temp = ''
    while N:
        temp = str(N % 2) + temp
        N //= 2

    count = [0]
    temp_count = 0
    for i in range(1, len(temp)):
        if temp[i - 1] != temp[i]:
            count.append(temp_count)
            temp_count = 1
        else:
            if temp[i] == '0':
                temp_count += 1

    if temp[-1] == 0:
        count[-1] = 0

    max_value = max(count)

    if max_value != 0:
        answer = max(count)

    return answer