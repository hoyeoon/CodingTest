# https://programmers.co.kr/learn/courses/30/lessons/60057 에서 실행
# 내가한 것
def solution(s):
    min_length = 1000

    for k in range(len(s) // 2 + 1):
        s += chr(k + 58)
    # print(s)

    for k in range(1, len(s) // 2 + 1):
        result = ""
        temp = ""
        count = 1
        # print("k = ", k)
        for i in range(len(s) // k):
            temp = s[i * k: (i + 1) * k]
            if s[i * k: (i + 1) * k] == s[(i + 1) * k: (i + 2) * k]:
                count += 1
            #   print("same")
            else:
                if count == 1:
                    result += temp
                else:
                    result += str(count)
                    result += temp
                temp = ""

                #   print(count)
                count = 1
            #   print("different")
        if min_length > len(result.split(':')[0]):
            min_length = len(result.split(':')[0])
    return min_length

# 해설 (더 좋아보임)
def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        result = ""
        temp = ""
        count = 1
        prev = s[0:step]
        for i in range(step, len(s), step):
            if prev == s[i: i + 1]:
                count += 1
            else:
                if count == 1:
                    result += temp
                else:
                    result += str(count) + temp


                #   print(count)
                count = 1

        # 남아 있는 문자열에 대해서 처리
        result += str(count) + temp if count >= 2 else temp

        answer = min(answer, len(result.split(':')[0]))
    return answer