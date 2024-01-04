# https://school.programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    answer = 0

    a = []

    for i in s:
        if len(a) > 0 and a[-1] == i:
            a.pop()
        else:
            a.append(i)

    if len(a) > 0:
        answer = 0
    else:
        answer = 1

    return answer

print(solution("baabaa"	))
print(solution("cdcd"))


