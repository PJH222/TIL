# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    fake_answer = []
    for i in range(1,10001):
        fake_answer.append(i)

    num = 0
    i = num

    while num <= n:
        if sum(fake_answer[num:i]) < n:
            i += 1
        elif sum(fake_answer[num:i]) == n:
            # print(fake_answer[num:i])
            answer += 1
            num += 1
            i = num

        else:
            num += 1
            i = num



    return answer

print(solution(15))
