import sys
sys.stdin = open('./input.txt')

T = int(input())
for _ in range(T):
    K,N,M = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(N)
    x = N
    answer = 0
    a.insert(0,0)
    #print(a)
    for i in range(N//K+3):
        for j in range(K,0,-1):
            if x - j in a:
                answer += 1
                x -= j
                break
    if answer < round(N//K):
        print(f'#{_ + 1} {0}')
        continue

    print(f'#{_+1} {answer-1}')


