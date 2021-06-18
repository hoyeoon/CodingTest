def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

list1.sort()

for i in list2:
    if binary_search(list1, i, 0, n - 1) is None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
