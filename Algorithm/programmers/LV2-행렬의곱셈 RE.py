# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = []
    arr2 = y_list(arr2)
    for j in arr1:
        stack1 = []
        for i in arr2:
            stack2 = []
            for k in range(len(arr1[0])):
                stack2.append(j[k]*i[k])
            stack1.append(sum(stack2))
            # print(stack2)
        answer.append(stack1)

    return answer

def y_list(arr2): # y=x 변환
    y = [[0 for i in range(len(arr2))] for j in range(len(arr2[0]))]

    for i in range(len(arr2)):
        for j in range(len(arr2[0])):
            y[j][i] = arr2[i][j]

    return y









print(solution([[1, 4], [3, 2], [4, 1]]	,[[3, 3], [3, 3]]	))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]]	,[[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
print(solution([[1, 4], [3, 2]]	,[[4, 5,6], [6, 9,3]]	))