def DFS(graph, v , visited,route):
    # 현재 노드를 방문처리
    global  all_routes
    visited[v] = True
    # print(visited)
    # print(v,end=' ')
    route.append(v)
    print(route)
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i ,visited,route)
        else:
            all_routes.append(route)
            route.clear()
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
all_routes = []
route = []
# 각 노드가 방문된 정보를 표현하기 위한 리스트
visited = [False] * 9

# DFS(graph,1,visited)
DFS(graph,2,visited,route)
# DFS(graph,3,visited)
# DFS(graph,4,visited)


print(all_routes)


# 기본적인 DFS의 개념이긴 한데, 깊이 우선인데, 얼마나 깊게 들어가는지 출력되게끔 하려면 어떻게 만들어야함??