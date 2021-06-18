s = input()
l_temp = list(s)
l = list(map(int, l_temp))

result = l[0]
for i in range(1, len(l)):
    if result * l[i] >= result + l[i]:
        result = result * l[i]
    else:
        result = result + l[i]
print(result)