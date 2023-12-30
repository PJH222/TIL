# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    answer = 0
    result = []

    for i in range(len(ingredient)):
        result.append(ingredient[i])
        if result[i-4:i] == [1,2,3,1]:
            answer+=1
            del result[-1:-5]
            print(result)





    return answer
print(f'#1',solution([2, 1, 1, 2, 3, 1, 2, 3, 1]	))
print('#2', solution([1, 3, 2, 1, 2, 1, 3, 1, 2]	))
print('#3', solution([1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]))