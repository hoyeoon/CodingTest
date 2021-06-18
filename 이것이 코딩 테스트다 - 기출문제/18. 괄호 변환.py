# 올바른 괄호 문자 판단 함수
def correct(l):
    count = 0
    for i in range(len(l)):
        if count < 0:
            return False
        if l[i] == '(':
            count += 1
        else:
            count -= 1
    return True


# 균형잡힌 괄호 문자열의 index 반환
def find_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i + 1
    return False


def solution(p):
    if correct(p) == True:
        return p

    if not p:
        return ''

    index = find_index(p)

    u = p[0:index]
    v = p[index:]

    print('u =', u)
    print('v =', v)

    if correct(u) == True:
        u += solution(v)
    else:
        temp = '('
        temp += solution(v)
        temp += ')'
        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        u = ''.join(u)
        u = temp + u

    print('result u =', u)

    return u