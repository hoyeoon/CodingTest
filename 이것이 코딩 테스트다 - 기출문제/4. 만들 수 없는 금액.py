# 정답
# n = int(input())
# l = list(map(int, input().split()))
# l.sort()
# target = 1
#
#
# for i in range(len(l)):
#     if target < l[i]:
#         break
#     target += l[i]
# print(target)

# 오답
# n = int(input())
# l = list(map(int, input().split()))
# l.sort()
#
# coin_list = [0] * 1000
#
# for i in range(len(l)):
#     coin_list[i] = l[i]
#
# result = 0
# for i in range(1000):
#     result += 1
#     if result in coin_list:
#         continue
#     if result not in coin_list:
#        if result < coin_list[0]:
#            print("정답 : ", 1)
#            break
#        else:
#            # print('i', i)
#            # print('result', result)
#            temp_result = result
#            for j in range(i, 0, -1):
#               temp_result -= coin_list[j - 1]
#
#               if temp_result < 0:
#                   temp_result += coin_list[j]
#                   continue
#               if temp_result == 0:
#                   # print("아직 정답아님", result)
#                   break
#
#            if temp_result != 0:
#                 print("정답 : ", result)
#                 break
