from collections import deque
def solution(n, computers):
    answer = 0
    que = deque()
    route = []
    for i in range(len(computers)):
        visited = [0] * (n)
        que = deque()
        que.append(i)
        visited[i] = 1 # [1 , 0 , 0] 즉 출발점은 1 임
        while que:
            a = que.popleft()
            for j in range(len(computers[a])):
                if visited[j] == 0 and computers[a][j] == 1:
                    visited[j] = 1
                    que.append(j)
        if visited not in route:
            route.append(visited)
    # print(route)
    return len(route)



print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))