from collections import deque

def bfs(maps,y,x):
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]

    que = deque()
    que.append((0,0))

    while que:
        y,x = que.popleft()
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]

            if yy < 0 or yy >= len(maps) or xx < 0 or xx >= len(maps[0]):
                continue

            if maps[yy][xx] == 0:
                maps[yy][xx] = maps[y][x] + 1
                que.append((yy,xx))

        if maps[len(maps) - 1][len(maps[0]) - 1] != 0:
            break

    # for i in maps:
    #     print(i)

def solution(maps):
    answer = 0

    for map in maps:
        for i in range(len(map)):
            if map[i] == 1:
                map[i] = 0
            else:
                map[i] = -1
    y,x = 0,0
    maps[0][0] = 1
    # print(maps)

    bfs(maps, y, x)

    return maps[len(maps)-1][len(maps[0])-1] if maps[len(maps)-1 ][len(maps[0])-1] != 0 else -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	))
print(solution([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,0,1]]	))

