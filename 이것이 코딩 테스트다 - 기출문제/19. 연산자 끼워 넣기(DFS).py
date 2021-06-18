n = int(input())
operand = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            print('add1 = ', add)
            dfs(i + 1, now + operand[i])
            add += 1 # DFS 연산을 한뒤 다시 돌아올 땐 다시 +1
            print('add2 = ', add)
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - operand[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * operand[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / operand[i])) # 나눌 때는 나머지 제거
            div += 1

print(add, sub, mul, div)
dfs(1, operand[0])

print(max_value)
print(min_value)