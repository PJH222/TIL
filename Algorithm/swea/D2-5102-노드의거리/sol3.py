import sys
sys.stdin = open('./input.txt')

def check(S,G):
    q = []
    # (위치, 최소 이동 간선 개수)
    q.append((S,0))
    # 방문했는가 표시
    visited = [0]*(V+1)
    visited[S] = 1
    while q:
        c,num = q.pop(0)
        # 현재 노드에서 갈 수 있는 경로 찾기
        for i in range(1, V + 1):
            # 연결되어 있고 방문하지 않은 노드라면 방문
            if adj[c][i] and not visited[i]:
                print(adj,i)
                # 도착했는가?
                if i == G:
                    return num+1
                q.append((i, num + 1))
                visited[i] = 1
    # 도착 못 함(S와 G가 연결되어 있지 않음)
    return 0

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # V : 노드의 개수, E : 방향성이 없는 간선
    V,E = map(int,input().split())

    # 인접행렬 : 간선 연결 확인
    # 노드 번호 1~V번
    adj = [[0]*(V+1) for _ in range(V+1)]

    # E개의 간선의 양쪽 노드 번호
    for _ in range(E):
        a,b = map(int,input().split())
        # 양쪽 다 표시
        adj[a][b] = 1
        adj[b][a] = 1

    # 출발 노드, 도착 노드
    S,G = map(int,input().split())

    # 최소 이동 간선 개수
    result = check(S,G)

    print(f'#{tc} {result}')