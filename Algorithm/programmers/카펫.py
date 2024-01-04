# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    a = brown + yellow

    for i in range(1,int(a**(1/2)*2)): #세로 길이
        for j in range(1,int(a**(1/2))+1900): #가로 길이
            if i * j == a and (i-1)*2 + (j-1)*2 == brown:
                if i not in answer or j not in answer:
                    answer.append(i)
                    answer.append(j)
                else:
                    return sorted(answer,reverse=True)

    print(int(a**(1/2))+10)


    return sorted(answer,reverse=True)


print(solution(10,2))
print(solution(8,1))
print(solution(24,24))