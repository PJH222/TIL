
# https://school.programmers.co.kr/learn/courses/30/lessons/12914

def combination(list):
    a = list[0]
    b = list[1]
    num = 1
    c = 1
    d = 1

    for i in range(a+1, a+b+1): #전체 갯수
        c *= i
        #a a
    for j in range(1, b+1): #2 갯수
        d *= j

    return c//d


def solution(n):
    answer = 0
    result = []

    for i in range(n+1):
        for j in range(n//2+2):
            if i + j*2 == n:
                result.append([i,j])
                #i : 1의 갯수, j : 2의 갯수

    for i in result:
        # print(i,combination(i))
        answer += combination(i)

    return answer%1234567





print(solution(4))
print(solution(3))
print(solution(1))
print(solution(5))
#5c0 + 4c1 + 3c2 = 1 + 4 + 3
