# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    strs = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    answer = ''
    strs_list = list(strs)

    for i in skip:
        for _ in range(3):
            strs_list.remove(i)

    for j in s:
        idx = strs_list.index(j)
        answer += strs_list[idx+index]



    return answer

print(solution("aukks"	,"wbqd"	,5))