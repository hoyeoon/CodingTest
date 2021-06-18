import copy

s = list(input())
s.sort()
s2 = copy.deepcopy(s)
sum = 0

i = 0
for i in range(len(s)):
    if 48 <= ord(s[i]) <= 57:
        sum += int(s[i])
        s2.remove(s[i])
        # del s2[i] -> s2 자체가 줄어들어서 원하는 값 안나옴.
        # print("i=", i, "s2:", s2)
    else:
        break
print(''.join(s2) + str(sum))
