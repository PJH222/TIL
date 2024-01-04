# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = 0
    num = n+1
    cnt = str(format(n,'b')).count("1")
    num_cnt = str(format(num,'b')).count("1")

    while cnt != num_cnt:
        num += 1
        num_cnt = str(format(num,'b')).count("1")

    answer = num




    return answer

print(solution(78))
print(solution(15))