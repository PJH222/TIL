import itertools

def solution(numbers):

    answer = ''
    result = []
    # for i in numbers:
    #     result.append([i,str(i) * 3])
    numbers.sort(reverse=True,key=lambda x: str(x) * 3)

    # for i,v in result:
    #     answer += str(i)

    return ''.join(str(number) for number in numbers) if ''.join(str(number) for number in numbers)[0] != '0' else "0"
    # numbers.sort(reverse=True, key=lambda x: str(x) * 3)  # 사전식 정렬 - 파이썬 특징
    # numbers = ''.join(str(s) for s in numbers)





    # return answer if len(answer) != answer.count("0") else "0"

print(solution([6, 10, 2]	))
print(solution([9,90,900,98,901]	))
print(solution([3,34,340,5,55,540]	))