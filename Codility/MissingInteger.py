def myfunc(mylist1):
    return sorted([x for x in mylist1 if x > 0])

def solution(A):
    target = 1
    A = myfunc(list(set(A)))
    # A.sort()

    for i in A:
        if target != i:
            break
        target += 1

    return target
