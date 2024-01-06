import sys
sys.stdin = open('./input.txt')

T = int(input())

for _ in range(T):
    answer = []
    ans = ''
    n = int(input())
    nlist = list(map(int,input().split()))

    a = sorted(nlist)[0:n//2]
    b = list(reversed(sorted(nlist)))[0:n//2]
    # print(a,b)

    for i in range(10):
        if i % 2 == 0:
            answer.append(b[i//2])
        else:
            answer.append(a[i//2])

    for i in answer:
        if answer.index(i) != n-1:
            ans += str(i) + ' '
        else:
            ans += str(i)
    print(f'#{_+1}',ans)
