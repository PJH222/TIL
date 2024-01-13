# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    # 지금 필요한 건, 순서에 대해 찾을 수 있어야 한다는 점
    # 우선적으로 뒤에 큰 숫자가 등장한다는지
    # 확인 할 수 있어야 한다는 점

    # 뒤에 있는 숫자 하나하나 대입하는 것이 아니라
    # 있는지 없는지를 확인할 수 있는 방법이 없을까??,,,
    # 뒤에는 현재 숫자와 같거나 작은 수는 세아릴 필요가 없음

    # 2차 시도
    # enumerate 활용해보자
    a = list(enumerate(numbers))
    for i in a:
        for j in a:
            if j[0] > i[0] and j[1] > i[1]:
                numbers[i[0]] = j[1]
                break
            numbers[i[0]] = -1

    return numbers




print(solution([2, 3, 3, 5]	))
print(solution([9, 1, 5, 3, 6, 2]	))
