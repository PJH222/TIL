# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    F = [0, 1]
    for i in range(n):
        F.append(F[-1]+F[-2])

    answer = F[-2] % 1234567





    return answer

print(solution(3))
print(solution(5))