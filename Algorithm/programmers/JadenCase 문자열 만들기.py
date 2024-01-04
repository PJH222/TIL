# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    answer = ''
    word = ''
    num = '0123456789'

    for i in s:
        for j in range(len(i)):
            if i[0] in num:
                word += i[j].lower()
                ind = 1
            else:
                word += i[j]
                ind = 0

            if ind == 1:
                answer += word.lower()
                word = ''
            else:
                answer += word.capitalize()
                word = ''


    return answer

print(solution("3people unFollowed me"	))
print(solution("for the last week"	))
