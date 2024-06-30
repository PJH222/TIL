# https://school.programmers.co.kr/learn/courses/30/lessons/12950


def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr1[0]))] for j in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    # print(answer)

    return answer

solution([[1,2],[2,3]],	[[3,4],[5,6]])