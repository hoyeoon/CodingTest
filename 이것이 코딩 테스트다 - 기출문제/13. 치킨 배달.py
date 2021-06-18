from itertools import combinations

n, m = map(int,input().split())
city = []

for i in range(n):
    city.append(list(map(int, input().split())))

# 거리구하기 함수
def distance(a, b):
    r = a[0] - b[0]
    c = a[1] - b[1]
    return abs(r) + abs(c)

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        if city[i][j] == 2:
            chicken.append([i, j])

# print(house)
# print(chicken)

disSumMin = 1313

# print(dfs_comb(chicken, 2))
# print(list(combinations(chicken, 2)))

new_chicken = list(combinations(chicken, m))
# print(new_chicken)
for c in new_chicken:
    # print(c)
    disSum = 0
    for k in range(len(house)):
        disMin = 101
        # 거리 계산
        for i in range(len(c)):
            if disMin > distance(house[k], c[i]):
                disMin = distance(house[k], c[i])
        disSum += disMin
    #    print(disMin)
    # print(disSum)
    if disSumMin > disSum:
        disSumMin = disSum
print(disSumMin)

# 입력 1
# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2
#
# 입력 2
# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
#
# 입력 3
# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

