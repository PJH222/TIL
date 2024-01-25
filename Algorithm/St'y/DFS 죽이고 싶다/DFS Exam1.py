def DFS(graph, v , visited):
    # 현재 노드를 방문처리
    global cnt
    visited[v] = True
    # print(visited)
    print(v,end=' ')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            DFS(graph, i ,visited)

# 각 노드가 연결된 정보를 하기 2차원 리스트 형태로 표현
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
cnt = 0
DFS(graph,1,visited)
# print("\n",cnt)
# 기본적인 DFS의 개념이긴 한데,