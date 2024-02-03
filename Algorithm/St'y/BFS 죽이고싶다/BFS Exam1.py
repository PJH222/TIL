# 너비 우선 탐색
# 출발에서부터 가까운 노드부터 우선 탐색
# 큐 자료구조를 이용
# 최단 거리 구하기

from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        # print(queue)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                # print(queue)
                visited[i] = True
        # print(queue)
graph = [
    [],         # 0번과 연결된, 사실 없는데, 답이 정돈되게 출력하기 위해 빈 리스트를 삽입한 것임.
    [2,3,8],    # 1번과 연결된 노드
    [1,7],      # 2번과 연결된 노드
    [1,4,5],    # 3번과 ...
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현하기 위한 리스트
visited = [False] * 9

bfs(graph,1,visited)
