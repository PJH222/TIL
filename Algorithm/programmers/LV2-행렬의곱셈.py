# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):

    y_arr1 = len(arr1)
    x_arr1 = len(arr1[0])

    y_arr2 = len(arr2)
    x_arr2 = len(arr2[0])

    answer = [[1 for i in range(x_arr2)] for i in range(y_arr1)]

    for i in range(x_arr1*y_arr1+x_arr2*y_arr2):
        pass

    print(answer)

    return answer


print(solution([[1, 4], [3, 2], [4, 1]]	, [[3, 3], [3, 3]]	))

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]]	, [[5, 4, 3], [2, 4, 1], [3, 1, 1]]	))

# 1 4             15 15     00 01
# 3 2    3 3    = 15 15     10 11    00 01
# 4 1    3 3      15 15     20 21    10 11 12  2*3*2

# 2 3 2     5 4 3       = 22 22 11
# 4 2 4     2 4 1       = 36 28 18
# 3 1 4     3 1 1       = 29 20 14 27 3*3*3

# 1 1    1 = 1
# 1 1    1 = 1  2*2*1