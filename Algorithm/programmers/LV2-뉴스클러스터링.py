# https://school.programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    A = {}
    B = {}
    AnB = [] # 교집합
    AuB = [] # 합집합

    for i in range(len(str1)-1):
        if (str1[i]+str1[i+1]).isalpha() == 1 and (str1[i]+str1[i+1]) not in A:
            A[str1[i]+str1[i+1]] = 1
        elif (str1[i]+str1[i+1]) in A:
            A[str1[i] + str1[i + 1]] += 1

    for i in range(len(str2)-1):
        if (str2[i]+str2[i+1]).isalpha() == 1 and (str2[i]+str2[i+1]) not in B:
            B[str2[i] + str2[i + 1]] = 1
        elif (str2[i] + str2[i + 1]) in B:
            B[str2[i] + str2[i + 1]] += 1
    # print(A,B), AnB는 어차피 한쪽에서만 판별해도 상관없음

    for i in A:
        if i in B:
            if A[i] < B[i]:
                for _ in range(A[i]):
                    AnB.append(i)
                for _ in range(B[i]):
                    AuB.append(i)
            else:
                for _ in range(B[i]):
                    AnB.append(i)
                for _ in range(A[i]):
                    AuB.append(i)
        
        if i not in B: #B에 없다면, 갯수만큼 합집합에 넣어주기
            for _ in range(A[i]):
                AuB.append(i)

    for i in B:
        if i not in AnB: #B에만 있는 것을 합집합에 넣어주기
            for _ in range(B[i]):
                AuB.append(i)
    # print(AnB,AuB)
    if len(AuB) == 0:
        answer = 65536
    else:
        answer = len(AnB) / len(AuB) * 65536


    # 합집합 만들때는 갯수 많은 쪽으로 계산해야함,,


    # 딕셔너리로 정리하는게 나은건가?


    return int(answer)

print(solution('FRANCE','french'))
print(solution('handshake','shake hands'	))
print(solution('aa1+aa2',	'AAAA12'))
print(solution('E=M*C^2',	'e=m*c^2'))