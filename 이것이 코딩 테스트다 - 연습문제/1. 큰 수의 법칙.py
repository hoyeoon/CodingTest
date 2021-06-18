answer = 0
n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort(reverse=True);
max_value = data[0]
second_value = data[1]

print(max_value)
print(second_value)

answer = (m // (k+1)) * (k * max_value + second_value) + (m % (k+1)) * max_value
print(answer)