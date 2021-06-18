n = list(map(int, input()))

half = len(n) // 2
sum1 = 0
sum2 = 0

for i in range(half):
    sum1 += n[i]
    sum2 += n[i + half]

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")