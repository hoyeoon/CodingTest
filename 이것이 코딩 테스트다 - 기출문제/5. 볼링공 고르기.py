n,m = map(int, input().split())
l = list(map(int, input().split()))

result = 0
for i in range(len(l) - 1):
    # print("i", i)
    for j in range(i + 1, len(l)):
        if l[i] != l[j]:
            result += 1
print(result)
