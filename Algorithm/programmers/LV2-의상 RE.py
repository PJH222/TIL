# https://school.programmers.co.kr/learn/courses/30/lessons/42578
import itertools

def solution(clothes):
    answer = 0
    diction = {}

    # dictionary 만들기
    for cloth, type in clothes:
        if type not in diction:
            diction[type] = [cloth]
        else:
            diction[type] += [cloth]

    if len(diction) == 1:
        return len(clothes)

    # for


    answer += len(clothes)
    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	))
print(solution([[1,1],[2,1],[1,2],[2,2],[3,1],[3,2]])) # 4 + 2c2 *
print(solution([[1,1],[2,1],[1,2],[2,2],[1,3],[2,3]]))
print(solution([[1,1],[2,1],[3,1],[4,1]]))
print(solution([[1,1],[2,2],[3,3],[4,4]]))