from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

n, x = map(int, input().split())
l = list(map(int, input().split()))

if count_by_range(l, x, x) == 0:
    print(-1)
else:
    print(count_by_range(l, x, x))