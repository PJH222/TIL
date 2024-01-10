# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    stack = ''
    result = []
    diction = {}

    for i in s:
        if i.isdigit() and len(stack) == 0:
            stack = i
            # print(stack)
        elif i.isdigit():
            stack += i
        elif i.isdigit() == 0 and len(stack) != 0:
            result.append(int(stack))
            stack = ''

    for i in result:
        if i not in diction:
            diction[i] = 1
        elif i in diction:
            diction[i] += 1

    word_list=sorted(diction.items(),key = lambda x:x[1],reverse = True)

    for i in word_list:
        answer.append(i[0])

    # print(s)


    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"	))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"	))
print(solution("{{20,111},{111}}"	))
print(solution("{{123}}"	))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"	))