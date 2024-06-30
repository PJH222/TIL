# https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = ''
    if n % 2 == 0:
        a = n // 2
        answer = '수박' * a
    else:
        a = (n - 1) // 2
        answer = '수박' * a + '수'
    print(answer)
    return answer

solution(3)
