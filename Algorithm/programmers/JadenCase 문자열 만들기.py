# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    answer = []
    word = '' #단어
    space = '' #빈공간
    num = '0123456789'
    indict = 0

    cnt = 0
    start = 0
    end = 0

    for i in range(len(s)-1):
        if s[i] != " " and cnt == 0:
            start = i
            cnt += 1

        elif s[i] == " ":
            if s[i+1] != " ":
                cnt = 0
                word = s[start:i+1]
                if word[0] in num:
                    answer.append(word.lower())
                else:
                    answer.append(word.capitalize())

        elif i == len(s)-2:
            # print(1)
            word = s[start:]
            if word[0] in num:
                answer.append(word.lower())
            else:
                answer.append(word.capitalize())
            print(word)

    if len(s.split()[-1]) <= 2:
        if s.split()[-1][0] not in num:
            answer.append(s.split()[-1].capitalize())
        else:
            answer.append(s.split()[-1].lower())

    return ''.join(answer)

print(solution("3people unFollowed 3e"	))
print(solution("for the last 3week"	))
print(solution("for the last     week"	))



