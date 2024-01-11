# https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0

    for i in permutations_4([1, -1], len(numbers)):
        a = 0
        for j in range(len(numbers)):
            a += i[j] * numbers[j]

        if a == target:
            answer += 1

    return answer

def permutations_4(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations_4(array, r-1):
                yield [array[i]] + next






print(solution([1, 1, 1, 1, 1],3	))
print(solution([4, 1, 2, 1],4	))