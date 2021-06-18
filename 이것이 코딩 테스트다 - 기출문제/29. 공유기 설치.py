n, c = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))
house.sort()

first = 1
last = house[-1]
result = 0

# for d in range(first, last + 1):
#     count = 1
#     location = house[0]
#     for i in range(1, len(house)):
#         if house[i] - location >= d:
#             count += 1
#             location = house[i]
#     if count < c:
#         break
#     result = count
#     print("distance : ", d)
#     print("count : ", count)

n, c = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))
house.sort()

first = 1
last = house[-1]

result = 0
while first <= last:
    mid = (first + last) // 2
    count = 1
    location = house[0]

    for i in range(1, len(house)):
        if house[i] - location >= mid:
            count += 1
            location = house[i]

    if count >= c:
        first = mid + 1
        result = mid
    else:
        last = mid - 1

print(result)