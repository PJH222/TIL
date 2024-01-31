from collections import deque

def solution(topping):
    answer = 0
    right = {}
    left = {}

    for i in topping:
        if i not in right:
            right[i] = 1
        else:
            right[i] += 1

    for i in topping:
        left[i] = 1
        right[i] -= 1
        if right[i] == 0:
            del right[i]

        # print(left,right)
        if len(left) == len(right):
            answer += 1
            # print("<<<<>>>>><<<<>>>>><<<<>>>>><<<<>>>>><<<<>>>>><<<<>>>>>")





    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]	))
print(solution([1, 2, 3, 1, 4]	))
print(solution([1, 2, 3, 4]	))
print(solution([1, 2, 3, 2, 4,5,7,6,3,2,3,6,6]	))
print(solution([1, 2, 1,2,1,2,1,2,1,2,1,2,1,2,1]	))