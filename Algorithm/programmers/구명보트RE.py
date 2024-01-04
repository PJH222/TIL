# https://school.programmers.co.kr/learn/courses/30/lessons/42885


def solution(people, limit):
    answer = 0
    #1 합쳐서 limit 되면 out
    #2 최소 + 최대 > limit 되면 최대만 out
    #3 최소 + 최대 < limit이면, 최소보다 더 크지만 최소 + 최대 < limit
    #3의 경우, 제일 최대로 큰 값인지 알 수 있는 방법이 있는가?

    # 스택 느낌으로 list하나 만들어서
    # 값 하나 넣고 또 다른 하나와의 합이 limit이 되게끔 만드는게 나으려나??
    # 근데 이렇게 하려면 remove로 하나씩 지워나가야하나?
    # 중복에 대한 제거가 안돼서 최적화가 안됨
    # 갇힌 사람 숫자가 5만명이라 for 문 두개 중첩 안됨

    # 해결하기 어려운 부분이, 합이 limit 보다 작은 경우임...
    people = sorted(people)
    x1 , x2 = 0 , len(people)-1 #이 방식으로 하면 지우지 않고 넘어갈 수 있음!
    while x2 >= x1:
        if people[x1] + people[x2] > limit:
            x2 -= 1
            answer += 1
        else:
            x2 -= 1
            x1 += 1
            answer += 1

    # print(x1 , x2)

    return answer

print(solution([70, 50, 80, 50]	,100))              #3
print(solution([70, 80, 50], 100))                   #3
print(solution([40,45,50,60,60,80,50]	,100))      #5
# 5 ,
print(solution([40,40,50,60,60]	,100))              #3
print(solution([40,30,50,70,60]	,100))              #3
print(solution([45,45,45,55]	,100))                  #2
print(solution([45]	,100))                          #1
print(solution([70,40,40,60,60]	,100))              #3