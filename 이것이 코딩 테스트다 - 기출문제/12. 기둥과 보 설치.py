# 설치, 삭제 가능 여부
def possible(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥이 설치된 경우
            # 바닥 위, '보의 한쪽 끝 부분 위', '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        elif a == 1:  # 보가 설치된 경우
            # '보의 끝 부분이 다른 기둥 위', '두 보의 사이'라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    result = []

    for i in range(len(build_frame)):
        x, y, a, b = build_frame.pop(0)

        if b == 1:  # 설치
            result.append([x, y, a])  # 먼저 설치해보고
            if possible(result) == False:  # 가능하지 않으면
                result.remove([x, y, a])  # ROLLBACK

        elif b == 0:  # 삭제
            result.remove([x, y, a])  # 먼저 삭제해보고
            if possible(result) == False:  # 가능하지 않으면
                result.append([x, y, a])  # ROLLBACK
    result.sort()
    return result