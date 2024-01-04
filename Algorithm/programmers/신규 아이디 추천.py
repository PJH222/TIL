# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    dot = '.'
    lis_dot = [] #. .. ... 의 집합
    eng = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    #1단계
    answer = new_id.lower()
    print("1단계",answer)

    answer22 = ''

    #2단계
    for i in answer:
        if i in eng:
            answer22 += i

    answer = answer22
    print("2단계",answer)

    #33
    answer22 = ''
    for i in answer:
        if i != '.':
            answer22 += i
        elif i == '.' and len(answer22) == 0:
            answer22 += i
        elif i == '.' and len(answer22) != 0 and list(answer22)[-1] != '.':
            answer22 += i
        elif i == '.' and len(answer22) != 0 and list(answer22)[-1] == '.':
            continue

    answer = answer22
    print("3단계", answer)

    #44
    answer22 = ''
    if len(answer) > 0:
        if list(answer)[0] == '.' and list(answer)[-1] == '.':
            for i in range(1,len(answer)-1):
                answer22 += list(answer)[i]

        elif list(answer)[0] == '.':
            for i in range(1,len(answer)):
                answer22 += list(answer)[i]

        elif list(answer)[-1] == '.':
            for i in range(len(answer)-1):
                answer22 += list(answer)[i]

        elif list(answer)[0] != '.' and list(answer)[-1] != '.':
            answer22 = answer
    print("4단계",answer22)
    answer = answer22

    #55
    if len(answer) == 0:
        answer = 'a'
    print("5단계",answer)

    #66
    if len(answer) > 15:
        answer22 = ''
        for i in range(15):
            if i != 14:
                answer22 += list(answer)[i]
            else:
                if list(answer)[i] != '.':
                    answer22 += list(answer)[i]
                else:
                    pass
    else:
        answer22 = answer

    answer = answer22
    print("6단계", answer)
    #77
    if len(answer) == 1:
        answer = answer * 3
    elif len(answer) == 2:
        answer += list(answer)[1]
    print("7단계",answer)



    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))