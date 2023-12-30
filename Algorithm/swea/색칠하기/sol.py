
import sys
sys.stdin = open('./input.txt')

T = int(input())





for _ in range(T):
    table = [[0 for i in range(10)] for j in range(10)]
    cnt = int(input())
    answer = 0
    for i in range(cnt):
        a = list(map(int,input().split()))

        for x in range(a[0],a[2]+1): #x가 움직이는 좌표
            for y in range(a[1],a[3]+1): #y가 움직이는 좌표
                if a[4] == 1:           #색깔 1 혹은 2로 분류하기
                    if table[y][x] == 2:
                        answer += 1
                    else:
                        table[y][x] = 1
                elif a[4] == 2:
                    if table[y][x] == 1:
                        answer += 1
                    else:
                        table[y][x] = 2
    #print(table)
    print(f'#{_+1} {answer}')
# 3
# 0 0 0 0 1
# 0 0 0 0 2
# 1 1 1 1 1