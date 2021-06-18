n, m = map(int, input().split())
array = list(map(int, input().split()))
start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total = total + x - mid
    if total == m:
        result = mid
        break
    elif total > m:
        start = mid + 1
    else:
        end = mid - 1

print(result)