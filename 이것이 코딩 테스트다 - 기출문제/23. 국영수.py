n = int(input())

students = []
for i in range(n):
    name, k, e, m = input().split()
    students.append((name, int(k), int(e), int(m)))

students = sorted(students, key=lambda student: (-student[1], student[2], -student[3], student[0]))

for student in students:
    print(student[0])