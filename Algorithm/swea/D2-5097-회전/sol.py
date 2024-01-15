import sys
from collections import deque

sys.stdin = open('./input.txt')

T = int(input())

for t in range(T):
    NM = list(map(int,input().split()))
    N = NM[0]
    M = NM[1]
    nlist = list(map(int,input().split()))
    a = M//N + 1
    nlist = nlist * a
    # nlist = deque()
    for i in range(M):
        del nlist[0]

    print("#{} {}".format(t+1,nlist[0]))

