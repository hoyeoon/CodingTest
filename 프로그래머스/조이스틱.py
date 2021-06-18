name = "JEROEN" # return 56
name2 = "JAN" # return 23

# 1. 각 알파벳에 대하여 최소 이동 값을 구한다. (make_name)
make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
print(make_name)

idx, answer = 0, 0
while True:
    answer += make_name[idx]
    make_name[idx] = 0

    # 2. 값이 0이면 알파벳을 바꿀 필요가 없는 것이다.
    if sum(make_name) == 0:
        break

    # 3. 좌우로 이동 방향을 정할 때 바꿔야하는 알파벳이 나오기까지 가장 짧은 거리를 구한다 (부분해)
    left, right = 1, 1
    while make_name[idx - left] == 0:
        left += 1
    while make_name[idx + right] == 0:
        right += 1

    # 4. 해당 방향으로 위치를 조절한다. 모든 리스트의 값이 0이 될 때까지 반복한다.
    if left < right:
        answer += left
    else:
        answer += right

    if left < right:
        idx += -left
    else:
        idx += right

print(answer)