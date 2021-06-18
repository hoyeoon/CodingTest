# input_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# output_num= [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = ['0'] * 101
dp[2] = '1'
dp[3] = '7'
dp[4] = '4'
dp[5] = '2'
dp[6] = '6'
dp[7] = '8'
dp[8] = '10'
dp[10] = '22'
dp[11] = '20'
dp[17] = '200'

for i in range(9, 101):
    if dp[i] != '0':
        continue
    dp[i] = dp[i - 7] + '8'

k = int(input())
for x in range(k):
    n = int(input())

    q = n // 2
    r = n % 2

    max_result = ''
    if r == 0:
        for i in range(q):
            max_result += '1'
    else:
        max_result += '7'
        for i in range(q - 1):
            max_result += '1'

    min_result = dp[n]

    print(min_result, max_result)