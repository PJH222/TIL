import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())

    # board = []
    # for _ in range(N):
    #     line = list(map(int,input().split()))
    #     board.append(line)

    board = [list(map(int,input().split())) for _ in range(N)]
    board_sum = 0
    max = 0
    for i in range(N-M+1):
        for j in range(N - M+1):
            for k in range(M):
                for l in range(M):
                    board_sum += board[i+k][j+l]
                    if board_sum > max:
                        max = board_sum

            board_sum = 0

    print(f'#{tc}',max)