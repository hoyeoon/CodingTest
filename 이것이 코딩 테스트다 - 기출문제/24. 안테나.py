n = int(input())
antena = list(map(int, input().split()))
antena.sort()

avg = (antena[0] + antena[-1]) // 2
# print(avg)

min_value = 1e9

l = []
for i in antena:
    min_value = min(abs(i - avg), min_value)
    l.append((i, min_value))
# print(min_value)
# print(l)

for i, j in l:
    if j == min_value:
        print(i)
        break