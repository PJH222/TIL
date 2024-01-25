import random

def dfs(x,y):
    if x <= -1 or y <= -1 or x >= n or y >= m: # 경계에서는 알아서 걸러짐
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1     # 검색한 원소에 대해서는 1로 방문 처리

        dfs(x - 1,y)        # 상하좌우가 0인지를 확인하여, 인접한 원소는 모두 1로 바꾸기
        dfs(x + 1, y)
        dfs(x , y - 1)
        dfs(x, y + 1)
        # print(graph)
        return True         # 모두 바꾸고 나서는 True로 반환
    return False

a = random.randint(3,4)

graph = [[random.randint(0,1) for i in range(a)] for j in range(random.randint(3,4))]

n = len(graph)
m = len(graph[0])

for i in graph:
    print(i)
result = 0

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if dfs(j,i) == True:    # 0을 모두 1로 변환한 한 덩어리를 만들때마다 1을 더해주기
            result += 1

print(result)
