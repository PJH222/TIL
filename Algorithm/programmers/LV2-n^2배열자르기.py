# https://school.programmers.co.kr/learn/courses/30/lessons/87390


# def double_dimension_table(n):
#     table = []
#     for i in range(1,n+1):
#         sub_table = []
#         for j in range(1,n+1):
#             if j >= i:
#                 sub_table.append(j)
#             elif j < i:
#                 sub_table.append(i)
#         for k in sub_table:
#             table.append(k)
#
#     return table

def solution(n, left, right):
    answer = []
    table = []
    cnt = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j >= i:
                cnt += 1
                if cnt >= left+1:
                    table.append(j)


                if cnt == right+1:
                    return table

            elif j < i:
                cnt += 1
                if cnt >= left+1:
                    table.append(i)


                if cnt == right+1:
                    return table
            # if cnt >= right +1:
            #     return table[left:right+1]



    return answer

print(solution(3,2,5))
print(solution(4,7,14))
# print(solution(10**7,0,10**8)) #<< 이거 안됨

# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5