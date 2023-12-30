import sys
sys.stdin = open('./input.txt')

T = int(input())
for _ in range(T):
    max = ''
    cnt = 0

    N = int(input())
    a = list(str(input()))
    a.sort(reverse=True)

    for i in a:
        if a.count(i) > cnt:
            max = i
            cnt = a.count(i)





    print(f'#{_+1}', max,cnt)