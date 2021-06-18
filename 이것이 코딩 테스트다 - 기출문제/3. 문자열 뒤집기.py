# s = list(input())
#
# count0 = 0
# count1 = 0
#
# if s[0] == '1':
#     count0 += 1
# else:
#     count1 += 1
#
# for i in range(len(s) - 1):
#     if s[i] == '1' and s[i + 1] == '0':
#         count1 += 1
#     elif s[i] == '0' and s[i + 1] == '1':
#         count0 += 1
#
# print(min(count0, count1))


# 정답

s = list(input())
count0 = 0
count1 = 0

if s[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))