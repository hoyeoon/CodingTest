t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    dp = []
    for i in range(1, n + 1):
        dp.append(l[m * (i - 1) : m * i])

    print(dp)

    # 순서 주의
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    print(dp)
    result = -1
    for i in range(n):
        for j in range(m):
            result = max(result, dp[i][j])

    print(result)


