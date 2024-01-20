import sys
sys.stdin = open('./input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    g = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        i, j = map(int, input().split())
        g[i].append(j)
        g[j].append(i)

    print(tc,g)
    S, G = map(int, input().split())
    # answer = bfs(S, G)
    # print('#{} {}'.format(tc, answer))