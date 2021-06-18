# 처음 위치를 찾는 이진 탐색 메서드
def first_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
            return mid
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

# 마지막 위치를 찾는 이진 탐색 메서드
def last_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

n, x = map(int, input().split())
l = list(map(int, input().split()))

print(first_search(l, x, 0, n - 1))
print(last_search(l, x, 0, n - 1))

if first_search(l, x, 0, n - 1) == -1 or last_search(l, x, 0, n - 1) == -1:
    print(-1)
else:
    print(last_search(l, x, 0, n - 1) - first_search(l, x, 0, n - 1) + 1)