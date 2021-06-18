# '#', '>', '<', '*'로 채워진 2차원 행렬 drum
# 첫 번째 행에서 출발하여 (0, 0), (0, 1) .... (0, n - 1)
# 가장 바닥(마지막 행)까지 도달하는 것들의 개수를 return
# '#'이면 아래로 이동.
# '>'이면 오른쪽 이동.
# '<'이면 왼쪽 이동.
# '*'가 첫번째 나오면 아래로 이동. 두번째 나오면 멈춤
# 정답 전체 맞아서 81/100 BUT 효율성 19점 중 0점 받음.
# 댓글 창을 보니 이모이제이션 사용해야하는 것으로 보임.

def solution(drum):
    size = len(drum)
    result = 0

    for j in range(size):
        flag = 0 # 두번째 * 표시위함
        i = 0

        while True:
            if i == size:
                result += 1
                break

            if drum[i][j] == '#':
                i += 1
            elif drum[i][j] == '>':
                j += 1
            elif drum[i][j] == '<':
                j -= 1
            elif drum[i][j] == '*':
                if flag == 1:
                    break
                i += 1
                flag = 1

    return result