import itertools

n = int(input())
operand = list(map(int, input().split()))
plus, minus, multiple, division = map(int, input().split())

operator = []
for i in range(plus):
    operator.append('+')
for i in range(minus):
    operator.append('-')
for i in range(multiple):
    operator.append('*')
for i in range(division):
    operator.append('/')

perm = itertools.permutations(operator, len(operand) - 1)
perm_l = list(perm)
perm_l = list(set(perm_l))

# print(len(perm_l))

min_result = 1e9
max_result = -1e9

for operator in perm_l:
    # print(operator)
    result = operand[0]
    for i in range(len(operand) - 1):
        if operator[i] == '+':
           result += operand[i + 1]
        elif operator[i] == '*':
            result *= operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
        elif operator[i] == '/':
            if result < 0:
                result = -result
                result = -(result // operand[i + 1])
            else:
                result //= operand[i + 1]
    min_result = min(min_result, result)
    max_result = max(max_result, result)

print(max_result)
print(min_result)