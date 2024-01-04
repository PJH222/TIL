# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    answer = 0
    sublist = []
    a = True
    b = len(ingredient)
    i = 0

    while i < b - 3:
        if ingredient[i:i+4] == [1,2,3,1]:
            del ingredient[i:i+4]
            b = len(ingredient)
            answer += 1
            if i > 4:
                i -= 3
            else:
                i = 0

        else:
            i += 1

        # print(i, ingredient)

    return answer


print(f'#1',solution([2, 1, 1, 2, 3, 1, 2, 3, 1]	))
print('#2', solution([1, 3, 2, 1, 2, 1, 3, 1, 2]	))
print('#3', solution([1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]))