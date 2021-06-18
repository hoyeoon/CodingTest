import copy

n = int(input())

dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

dp.sort(key=len, reverse=True)
array = copy.deepcopy(dp)

for i in range(1, n):
    j = 0
    while j < n - i:
        dp[i][j] += max(dp[i-1][j], dp[i-1][j+1])
        print(dp[i][j], end=' ')
        j += 1
    print()
print(dp)
print('result = ', dp[n - 1][0])