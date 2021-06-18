m, n, k = map(int, input().split())

space = [[0] * n] * m
print(space)

for i in range(k):
    a, b, c, d = map(int, input().split())

    x, y = m - d, a
    print(x, y)
    print(c - 2, n - b - 2)
    print('----------')
    for p in range(x, c - 1):
        for q in range(y, n - b - 1):
            print(p,q)
            space[p][q] = 1

    print(space)
print("**********")
print(space)