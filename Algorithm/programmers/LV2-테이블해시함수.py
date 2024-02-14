# https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(reverse=True)
    data.sort(key=lambda x: x[col - 1])
    # S_2 = data[2][0] // 2, data[2][1] // 2 , data[2][2] // 2

    numbers = []
    for i in range(row_begin - 1, row_end):
        result = 0
        for j in range(len(data[i])):
            result += (data[i][j] % (i + 1))
        answer ^= result

    # answer = []
    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]]	,2,2,3,4))