# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    # print(list(reversed(sorted(citations))))
    a = list(reversed(sorted(citations)))
    le = len(a)

    for i in range(le):
        if len(a[0:i+1]) <= a[i]:
            pass
        else:
            return i

    return le

print(solution([3, 0, 6, 1, 5]	))
print(solution([9, 7, 6, 2, 1]))
print(solution([3, 3, 3, 4, 4]))
print(solution([7, 7, 6, 7, 6]))