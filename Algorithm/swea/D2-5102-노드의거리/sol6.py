from collections import deque

import sys
sys.stdin = open('./input.txt')

t = int(input())
for tc in range(1, t + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    # route = [[] for _ in range(v + 1)]
    for i in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    s,g = map(int,input().split())

    visited = [0] * (v + 1)
    que = deque()
    que.append(s)
    visited[s] = 1
    cnt = 0
    while que:
        # print(que)
        a = que.popleft() # 내가 다녀갔었던 곳을 지우려면 popleft해야함...
        for i in graph[a]:
            if visited[i] == 0:
                que.append(i)
                # route[a].append(i)
                visited[i] = visited[a] + 1

        if visited[g] != 0:
            que.clear()

        # print(visited)
    print(graph)
    # print(route)
    if visited[g] != 0:
        print("#{} {}".format(tc,visited[g] - 1))
    else:
        print("#{} {}".format(tc, 0))




