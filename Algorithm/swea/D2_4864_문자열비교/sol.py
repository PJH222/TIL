import sys
sys.stdin = open('./input.txt')

T = int(input())

for _ in range(T):
    N = str(input())
    M = str(input())
    if N in M:
        print(f'#{_+1}',1)
    else:
        print(f'#{_ + 1}', 0)