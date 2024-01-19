import sys
sys.stdin = open('./input.txt')

def DFS(i,sm):
    global answer
    if answer <= sm:
        return
    global cnt
    if i == N:
        answer = min(sm, answer)
        return

    for j in range(N):
        cnt +=1
        if check[j] == 0:
                check[j] = 1
                DFS(i+1,sm+table[i][j])
                check[j] = 0
                print(cnt)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N) ]
    answer = 9 * N
    check = [0 for i in range(N)]
    cnt = 0
    DFS(0,0)
    print('#{} {}'.format(tc,answer))
