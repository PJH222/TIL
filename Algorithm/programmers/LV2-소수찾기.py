import itertools

def solution(numbers):
    result = []
    answer = 0
    for i in range(1,len(numbers)+1):
        for j in list(map(''.join,itertools.permutations(numbers,i))):
            if int(j) == 1 or int(j) == 0:
                continue
            if int(j) not in result:
                result.append(int(j))
                answer += find_number(int(j))
    # print(result)

    return answer

def find_number(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1


print(solution("17"))
print(solution("011"))
print(solution("21"))