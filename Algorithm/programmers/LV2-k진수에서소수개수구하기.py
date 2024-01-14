# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    answer = 0
    number = asd(n,k)
    find_number = []
    # print(number)
    # print(number)
    lis = str(number).split("0")
    # print(lis)
    if lis.count("") > 0:
        a = lis.count("")
        for _ in range(a):
            lis.remove("")

    for i in lis:
        answer += find(int(i))
        print(i,find(int(i)))
        # print(i)

    return answer

def asd(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

def find(n):
    if n == 1:
        return 0

    cnt = 0
    for i in range(2,int(n**0.5)+5):
        if n%i == 0 and n == i:
            # print(i)
            cnt += 1
            if cnt == 1:
                return 1
        elif n%i == 0:
            cnt += 1

    if cnt == 0:
        return 1

    return 0


# # print(solution(45, 3))
# print(solution(437674,	3))
# print(solution(110011	,10	))
# print(solution(4,2))
# print(solution(355353,10))
# print(solution(355353,8))
print(solution(9,10))