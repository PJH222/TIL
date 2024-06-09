# https://school.programmers.co.kr/learn/courses/30/lessons/42748



def solution(array, commands):
    answer = []
    
    for i in commands:
        start = i[0]
        end = i[1]
        index_number = i[2]
        new_array = array[start-1:end]
        new_array = sorted(new_array)
        answer.append(new_array[index_number - 1])
        
    
    return answer


solution([1, 5, 2, 6, 3, 7, 4]	,[[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    