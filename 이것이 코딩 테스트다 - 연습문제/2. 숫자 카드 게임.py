answer = 0
n, m = map(int, input().split())
max_value = 0;

for i in range(n):
    data = list(map(int, input().split()))

    if max_value < min(data):
        max_value = min(data)

print(max_value)