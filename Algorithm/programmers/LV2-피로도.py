# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    result = dfs_perm(dungeons,n)
    max = 0
    # print(result)
    for i in result:
        a = k
        cnt = 0
        for j in range(len(i)):
            if a >= i[j][0] and a >= i[j][1]:
                a -= i[j][1]
                cnt += 1
                if cnt == len(i):
                    return len(i)

            elif a < i[j][0] or a < i[j][1]:
                break

        if max < cnt :
            max = cnt

    return max

def dfs_perm(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack = []
    for i in idx:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()

        for i in idx:
            if i not in cur:
                temp = cur + [i]
                if len(temp) == n:
                    element = []
                    for i in temp:
                        element.append(lst[i])
                    ret.append(element)
                else:
                    stack.append(temp)
    return ret




print(solution(80,[[80,20],[50,40],[30,10]]	))
print(solution(80,[[80,20],[50,40]]	))
print(solution(80,[[80,20],[50,40],[80,20],[50,40]]	))
# print(solution(80,[[80,80],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]	))
# print(dfs_perm([1,2,3,4],3))