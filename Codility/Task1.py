# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(T):
    T = float(T)
    if T < 35:
        answer = 'hypothermia'
    elif 35 <= T <= 37.5:
        answer = 'normal'
    elif 37.5 < T <= 40:
        answer = 'fever'
    else:
        answer = 'hyperpyrexia'
    return answer