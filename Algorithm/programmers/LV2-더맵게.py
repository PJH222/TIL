# https://school.programmers.co.kr/learn/courses/30/lessons/42626

# def solution(scoville, K):
    #이상하게 dictionary를 사용하지 않으면 모조리 시간초과 발생한다...ㅠㅠㅠ
    # diction = {}
    # k = 0
    # # scoville.sort()
    # for i in scoville:
    #     if i not in diction:
    #         diction[i] = 1
    #     else:
    #         diction[i] += 1
    #
    #
    # for i,v in list(diction.items()):
    #     if len(list(diction.items())) >= 2:
    #         # print(diction.keys())
    #         a1 = min(list(diction.keys()))
    #         diction[a1] -= 1
    #         if diction[a1] == 0:
    #             del diction[a1]
    #
    #         a2 = min(list(diction.keys()))
    #         diction[a2] -= 1
    #         if diction[a2] == 0:
    #             del diction[a2]
    #
    #         if a1 + a2 * 2 not in diction:
    #             diction[a1 + a2 * 2] = 1
    #             k += 1
    #         else:
    #             diction[a1 + a2 * 2] += 1
    #             k += 1
    #
    #     if min(diction) >= K:
    #         return k
    #
    #     if len(diction) < 2:
    #         return -1

        # diction[i] -= 1
        # if diction[i] == 0:
        #     del diction[i]
        # print(diction)




#
#     # 스택 도전 2
#     dict = {}
#     k = 0
#
#     scoville.sort(reverse=True)
#
#     for i in scoville:
#         a1 = scoville.pop()
#         a2 = scoville.pop()
#         scoville.append(a1 + a2 * 2)
#         k += 1
#         arr(scoville)
#         if scoville[-1] >= K:
#             return k
#
# def arr(list):
#     for i in range(1,len(list)):
#         if list[-1 * i] > list[-1 * (i+1)]:
#             a = list[-1 * (i+1)]
#             b = list[-1 * (i)]
#             list[-1 * i] , list[-1 * (i+1)] = a , b
#         else:
#             return list






    # scoville을 dictionary로 변경
    # scov = sorted(scoville, reverse=True)
    #
    # for i in range(len(scoville)-1):
    #     scov = sorted(scov, reverse=True)
    #     if scov[-1] >= K:
    #         return k
    #
    #     a1 = scov.pop() #가장 작은 값
    #     a2 = scov.pop() #두번째로 작은 값
    #     scov.append(a1 + a2 * 2)
    #     k += 1
        # print(scov)
    # 효율성 실패
    #
    # stack 낭낭하게 채워보자~~

# def solution(scoville, K):
#     dict = {}
#     cnt = 0
#
#     for i in scoville:
#         if i not in dict:
#             dict[i] = 1
#         else:
#             dict[i] += 1
#
#     for key in range(len(dict)): #한번에 섞는 방법은 없는가??
#         print(sum(dict)*3 )
#         if min(dict) >= K:
#             return cnt
#
#         if len(dict) >= 2:
#             a1 = min(dict)
#             dict[a1] -= 1
#             if dict[a1] == 0:
#                 del dict[a1]
#
#             a2 = min(dict)
#             dict[a2] -= 1
#             if dict[a2] == 0:
#                 del dict[a2]
#
#             cnt += 1
#
#             a3 = min(a1,a2) + max(a1,a2) * 2
#             if a3 not in dict:
#                 dict[a3] = 1
#             else:
#                 dict[a3] += 1
#         else:
#             return -1
def dict2(list):
    dict = {}
    for i in list:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict


def solution(scoville,K,cnt=0):
    dict = dict2(scoville)
    z = sorted(dict)

    for i in z:
        if len(z) > 2:
            a1 = z[0]
            a2 = z[1]
            if a1 >= K:
                return cnt
            cnt += 1
            a3 = min(a1,a2) + max(a1,a2) * 2
            dict[a1] -= 1
            if dict[a1] == 0:
                del dict[a1]

            dict[a2] -= 1
            if dict[a2] == 0:
                del dict[a2]

            if a3 not in dict:
                dict[a3] = 1

            else:
                dict[a3] += 1

            return solution(list(dict.keys()), K)
        else:
            return -1







        # else:
        #     if len(dict) >= 2:
        #         scove = min(stack) + max(stack) * 2
        #         dict[max(stack)] -= 1
        #         if dict[max(stack)] == 0:
        #             del dict[max(stack)]
        #
        #         dict[min(stack)] -= 1
        #         if dict[min(stack)] == 0:
        #             del dict[min(stack)]
        #
        #         if scove not in dict:
        #             dict[scove] = 1
        #         else:
        #             dict[scove] += 1
        #         stack = []
        #         stack.append(key)


# 1 2 3 9 10 12 / 1 4 6 18 20 22
# 3 5 9 10 12
# 9 10 12 13
# 12 13 29
# 29 38
# 105

print(solution([1, 2, 3, 9, 10, 12]	,7))
print(solution([1, 2, 3, 12, 10, 8]	,7))
# print(test({1:2, 3:4}))