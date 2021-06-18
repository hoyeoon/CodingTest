n = int(input())
list1 = set(map(int, input().split()))  # list가 아니라 set을 쓰자.
m = int(input())
list2 = list(map(int, input().split()))

print(list1)

for i in list2:
    if i in list1:
        print("yes", end=' ')
    else:
        print("no", end=' ')