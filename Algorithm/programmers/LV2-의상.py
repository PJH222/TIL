# https://school.programmers.co.kr/learn/courses/30/lessons/42578

#정확하게 계산하는 것보다, 범위가 작기 때문에,
# 오히려 모든 리스트를 만들어서 갯수 세는 것이 빠를 것 같다..
def solution(clothes):
    answer = 0
    diction = {}
    for cloth in clothes:
        if cloth[1] not in diction:
            diction[cloth[1]] = 1
        else:
            diction[cloth[1]] += 1

    for v in diction.values(): #key는 안중요하다,,
        for k in diction.keys():
            for i in clothes:
                answer += 1
                if answer > 500:
                    continue
                else:
                    pass


    return answer


def factorial(list): #종류별로 갯수만 들어 있는 리스트
    answer = 0
    return 0




print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	))
#2c1 + 3c2 = 3 + 2
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	))
#3c1 + 0 = 3
# 상의-ㄱ ㄴ ㄷ
# 하의-ㅏ ㅑ
# 5c1 +

# 겉옷 -1 2 3
# 얼굴 - a
#1종류 입을때, 아무거나 1개
#2종류 입을때, 3*2 + 3*3 + 3*1 +
#얼굴 - 1 2
#안경 - 5
#1종류 입을때, 3
#2종류 입을때, 2c2 * 2 * 1