'''

def dfs(visited, v, route):
    pass


graph = ['101010','111111','000001','111111','111111']

n = len(graph)
m = len(graph[0])

cnt_1 = 0
min = 0

y,x = 0,0
end_y,end_x = n,m
route = []

for i in graph:
    cnt_1 += i.count("1")


visited = [0] * cnt_1
'''

'''
graph = [[1,0,0],
         [1,1,1],
         [0,0,1]]
이런 형태로 그래프가 주어지고,
0,0 에서 n,m으로 이동할 때 최단 거리를 구하라...

힌트)
BFS를 활용해서
최단 거리를 구하는 경우의 수를 구했던 노가다 방식대로
만들면 된다. 


'''



from collections import deque
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4): # 4방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1: # 1일 경우에만 반응...
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                
    return graph[n-1][m-1]

# graph = [[1,0,0],
#          [1,1,1],
#          [0,0,1]]


graph = [[1,1,1,1,0],
         [1,1,0,1,0],
         [0,0,0,1,0],
         [1,1,1,1,0],
         [1,1,1,1,1]]


n = len(graph)
m = len(graph[0])

dy = [0,0,-1,1]
dx = [-1,1,0,0]


print(bfs(0,0))

for i in graph:
    print(i)

