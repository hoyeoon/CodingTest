n = int(input())
list1 = [0] * 1000000

for i in input().split():
    list1[int(i)] = 1

m = int(input())
list2 = list(map(int, input().split()))

print(list1)

for i in list2:
    if list1[i] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')