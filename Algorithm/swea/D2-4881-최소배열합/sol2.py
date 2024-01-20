import sys
sys.stdin = open('./input.txt')

def DFS(cnt,sum_min):
    global answer
    if sum_min >= answer:
        return


    if cnt == N:
        answer = min(answer,sum_min)
        return

    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            DFS(cnt+1,sum_min+a[cnt][i])
            check[i] = 0
            if cnt != N and answer < sum_min:
                break
            # print(i,answer)

T = int(input())

for t in range(1,T+1):
    N = int(input())
    a = [list(map(int,input().split())) for i in range(N)]
    check = [0 for i in range(N)]
    answer = N * 9
    DFS(0,0)
    print('#{} {}'.format(t,answer))
