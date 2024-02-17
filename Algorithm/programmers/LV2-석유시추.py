# https://school.programmers.co.kr/learn/courses/30/lessons/250136

import sys
sys.setrecursionlimit(1000000)
# 이거 때문에 틀리는 건가...??

from copy import deepcopy


def bfs(x, y, land):
    global cnt, indict, alpha, alpha_index

    if x < 0 or y < 0 or x >= len(land[0]) or y >= len(land) or land[y][x] != 1:
        return

    if land[y][x] == 1:
        land[y][x] = alpha_index  # 여기서 한번 바뀌고 나면 숫자가 안바뀌어야 할 거 같은데... 왜 자꾸 바뀌는거지??
        cnt += 1

    bfs(x + 1, y, land)
    bfs(x - 1, y, land)
    bfs(x, y + 1, land)
    bfs(x, y - 1, land)
    return
    # indict += 1


# 효율성 테스트가 있어서, 한뭉탱이 인지 방법이 중요한거 같은데...
# 한뭉탱이를 구별하는 방법이 뭐가 있지??

def solution(land):
    global cnt, indict, alpha, alpha_index

    alpha_index = 2
    answer = 0
    result = 0
    diction = {}

    # 석유 있는 위치가 1,
    # 비어 있는 위치가 0,
    maxx = 0
    # a = deepcopy(land)

    for x in range(len(land[0])):
        stack = []

        result = 0

        for y in range(len(land)):  # y방향으로 먼저 들어가기...
            cnt = 0
            bfs(x, y, land)

            if land[y][x] == 0:
                continue

            if land[y][x] not in diction:
                diction[land[y][x]] = cnt

            if land[y][x] not in stack:
                stack.append(land[y][x])

            alpha_index += 1

            # for i in land:
            #     print(i)
            # else:
            #     print()

        else:
            # print(stack)
            for i in stack:
                result += diction[i]

            if result > maxx:
                maxx = result

            # for i in land:
            #     print(i)
            # else:
            #     print()

    # print(diction)
    return maxx