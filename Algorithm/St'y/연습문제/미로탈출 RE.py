'''
<미로탈출 문제 설명>
n x m 사이즈인 graph가 주어질때,

예시)graph = [[1,0,0],
             [1,1,1],
             [0,0,1]]

예시와 같은 형태로 그래프가 주어지고,
graph[0][0]에서 graph[n][m]으로 이동할 때 최단 거리를 구하라...

--조건
1. graph[0][0] , graph[n][m] = 1 , 1
2. graph 상에서 1은 지나갈 수 있는 길 이라고 가정할 것
3. graph 상에서 0은 지나갈 수 없음
'''



from collections import deque

def bfs(y,x):
    sub = deque()
    sub.append((y,x))
    global cnt
    while sub:
        y,x = sub.popleft()
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]

            if yy < 0 or xx < 0 or yy >= n or xx >= m:
                continue

            if graph[yy][xx] == 0:
                continue

            if graph[yy][xx] == 1:
                sub.append((yy,xx))
                graph[yy][xx] = graph[y][x] + 1
            cnt += 1
        # 최적화
        if graph[n-1][m-1] != 1:
            return



graph = [[1,1,1,1,0],
         [1,1,0,1,0],
         [0,0,0,1,0],
         [1,1,1,1,0],
         [1,1,1,1,1]]

graph = [[1,0,0],
        [1,1,1],
        [0,0,1]]

graph = [[1,0,1,1],
        [1,1,1,0],
        [1,0,1,1]]



n = len(graph)
m = len(graph[0])

dx = [0,0,-1,1]
dy = [1,-1,0,0]
cnt = 0
bfs(0,0)
for i in graph:
    print(i)
print(cnt)

# 이거 근데 왜 [0][0]이 3으로 바뀌는거지??


