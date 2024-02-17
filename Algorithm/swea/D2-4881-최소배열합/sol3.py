import sys
sys.stdin = open('./input.txt')

def dfs(cnt, summ):
    global answer, visitied
    if summ >= answer:
        return
    if N == cnt:
        answer = min(summ, answer)
        return
    for i in range(N):
        if visitied[i] == 0:
            visitied[i] = 1 # 방문함
            dfs(cnt + 1, summ + a[cnt][i])
            visitied[i] = 0
            # stack.append(a[cnt][i])


for t in range(int(input())):
    stack = []
    N = int(input())
    answer = N * 9
    a = [list(map(int,input().split())) for i in range(N)]
    visitied = [0 for i in range(N)]
    dfs(0,0)
    print(answer,stack)