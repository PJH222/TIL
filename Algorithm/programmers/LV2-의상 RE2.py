# 미친,,, 문제를 잘 못이해하고 풀고있었다...
# 입지않는 경우 0 을 추가하여 생각하면 걍 답 나옴
# key값을 위치라고 생각하고 바라보면
# 이 문제는 조합이 아닌 순열 문제임...
# return 에서 -1하는 이유는 "모두 안입었을 경우"임
def solution(clothes):
    answer = 1
    diction = {}
    for val,key in clothes:
        if key not in diction:
            diction[key] = [val]
        else:
            diction[key] += [val]

    for val in diction.values():
        answer *= len(val) + 1

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	))
# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	))
# print(solution([[1,1],[2,1],[1,2],[2,2],[3,1],[3,2]])) # 4 + 2c2 *
# print(solution([[1,1],[2,1],[1,2],[2,2],[1,3],[2,3]]))
# print(solution([[1,1],[2,1],[3,1],[4,1]]))
# print(solution([[1,1],[2,2],[3,3],[4,4]]))