# https://school.programmers.co.kr/learn/courses/30/lessons/84512

# a = ['a','b','aa','ab','aaa','aab']
#
# print(sorted(a))
# 중복 순열로 모든 경우를 구하고 이를 sort하여 순서 구하기
def solution(word):
    result = []
    moum = ['A','E','I','O','U']
    for r in range(1,6):
        for i in perm2(moum,r):
            result.append(''.join(i))
    result.sort()
    # print(result)
    answer = result.index(word)
    return answer + 1


def perm(moum):
    result = []
    a = ''

def perm2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in perm2(array, r-1):
                yield [array[i]] + next

print(solution("AAAAE"	))