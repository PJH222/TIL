# 이번에는 최단 거리에 있는 루트 전체를 뽑아보기

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
    while que:
        a = que.popleft()
        for i in graph[a]:
            if visited[i] == 0: # bfs 방식이라 그런건가...
                visited[i] = visited[a] + 1
                # visited[i] = 1
                que.append(i)

            if visited[g] != 0:
                break

        if visited[g] != 0:
            break

    que.clear()
    que.append(g)
    cnt = visited[g]
    answer = [g]
    while que:
        a = que.popleft()
        for i in graph[a]:
            if visited[i] == cnt - 1:  # bfs 방식이라 그런건가...
                cnt -= 1
                # visited[i] = 1
                que.append(i)
                answer.append(i)
                # 이 방법이 유효한 이유는 cnt와 같지않으면 추가 자체가 안됨
                # print(123232)

        if cnt == 1:
            # print(43434)
            break
    print(s,g)
    print(answer)

    print(visited)
    print(graph)


    