# https://programmers.co.kr/learn/courses/30/lessons/60059 에서 실행
# #
# key = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]#
# lock = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# # if test == test2
#
# # a = [[1] * len(test) for _ in range(len(test))]
# # print(a)
#
# key_len = len(key) - 1
# lock[0][0] += key[key_len - 4][key_len]
# print(lock)
#
import copy

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

total_length = 2 * len(key) + len(lock) - 2
lock_length = len(lock)
key_length = len(key)

origin_lock = lock

print(total_length)



for i in range(4):
    key = rotate_90(key)
    lock = copy.deepcopy(origin_lock)
    temp = [0] * total_length
    print('lock = ', lock)

    # 2 회 = len(key) - 1
    for j in range(key_length - 1):
        lock.insert(0, temp)
        lock.append(temp)
    # print('lock = ', lock)
    # for j in range(total_length):
    #     lock[j].append(0)
    #        # lock[total_length - j].append(0)
    print(key_length)
    for j in range(key_length - 1, key_length - 1 + lock_length):
        for k in range(key_length - 1):
            lock[j].insert(0, 0)
            lock[j].append(0)

    #
    # for p in range(key_length - 1 + lock_length):
    #     for q in range(key_length - 1 + lock_length):
    #         for x in range(key_length):
    #             for y in range(key_length):
    #                 lock[p + x][q + y] += key[x][y]

    padding_lock = copy.deepcopy(lock)
    print(padding_lock)

    for p in range(key_length - 1 + lock_length):
        for q in range(key_length - 1 + lock_length):
            for x in range(key_length):
                for y in range(key_length):
                    lock[p + x][q + y] += key[x][y]

      #      print(lock)

            flag = 1
            for j in range(key_length - 1, key_length - 1 + lock_length):
                for k in range(key_length - 1, key_length - 1 + lock_length):
                    if lock[j][k] != 1:
                        flag = 0
                        break
            if flag == 1:
                result = "true"
            else:
                result = "false"
            print(result)

            lock = copy.deepcopy(padding_lock)
    #        print(lock)
