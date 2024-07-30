
from itertools import combinations as cc
def solution(nums):
    answer = 0

    tmp = [] # 소수 들의 리스트

    for i in range(2,int(30000000 ** 0.5) + 1):
        for j in range(2,i + 1):
            if i % j == 0 and i != j:
                break
        else:
            tmp.append(i)

    a = cc(nums, 3)

    for i in a:
        if sum(i) in tmp:
            answer += 1

    # 3개씩 묶어서 더하는 방법을 어떻게 만들지??
    print(answer)

    return answer

solution([1,2,3,4])
solution([1,2,7,6,4])

