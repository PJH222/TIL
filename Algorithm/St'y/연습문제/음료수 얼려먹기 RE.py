'''
<문제 설명>

그래프가 주어졌을 때,
그래프에서 0으로 이어진 덩어리를 1개라고 볼 경우에,
그래프 내에 몇 덩어리가 있는지 확인하는 알고리즘을 만들어라.

--조건
그래프 size = 2x2 ~ 1000x1000

'''

import random

a = random.randint(3,4)

graph = [[random.randint(0,1) for i in range(a)] for j in range(random.randint(3,4))]

# graph = [[1,0,0,0],
#          [0,1,1,1],
#          [1,0,0,0]]

def bfs(y,x):
    global cnt

    cnt += 1
    if y < 0 or x < 0 or y >= len(graph) or x >= len(graph[0]):
        return False

    if graph[y][x] == 0:
        graph[y][x] = 1
        # bfs(y+1,x)
        # bfs(y-1, x)
        # bfs(y, x+1)
        # bfs(y, x-1)

        for i in range(4):
            bfs(y+dy[i],x+dx[i])
        return True
    return False


for i in graph:
    print(i)

answer = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if bfs(i,j):
            answer += 1



print(answer, cnt)