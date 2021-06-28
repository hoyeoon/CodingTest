from math import *

def solution(inner, outer, points_x, points_y):
    answer = 0
    n = len(points_x)

    for i in range(n):
        if inner < sqrt(pow(points_x[i], 2) + pow(points_y[i], 2)) < outer:
            answer += 1

    return answer