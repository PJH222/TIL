import sys
sys.stdin = open('./input.txt')


T = int(input())

for _ in range(T):
    answer = 0
    table = []
    cnt = 0
    N, K = map(int,input().split())

    for i in range(N):
        a = list(map(str,input().split()))
        table.append(a)
        for j in range(len(a)):
            if j==0 and ''.join(a[j:j+K+1]) == '1' * K + '0':
                answer += 1
            elif j == N-K and ''.join(a[j-1:j+K]) == '0'+'1' * K:
                answer += 1
            elif 0<j<N and ''.join(a[j-1:j+K+1]) == '0' + '1'*K + '0':
                answer += 1
    table_t = [[0 for i in range(N)] for j in range(N)]

    for x in range(N):
        for y in range(N):
            table_t[x][y] = table[y][x]

    for l in table_t:
        for j in range(len(a)):
            if j==0 and ''.join(l[j:j+K+1]) == '1' * K + '0':
                answer += 1
            elif j == N-K and ''.join(l[j-1:j+K]) == '0'+'1' * K:
                answer += 1
            elif 0<j<N and ''.join(l[j-1:j+K+1]) == '0' + '1'*K + '0':
                answer += 1

    print(f'#{_+1} {answer}')






