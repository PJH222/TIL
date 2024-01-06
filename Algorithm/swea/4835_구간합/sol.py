import sys
sys.stdin = open('./input.txt')


T = int(input())

for z in range(1,T+1,1):
    limit = list(map(int,input().split()))
    N = limit[0]
    M = limit[1]
    numbers = list(map(int, input().split()))
    min_sum = sum(numbers)
    max_sum = 0
    x = 0 #x 좌표

    for i in range(N-M+1):
        if sum(numbers[i:i+M]) > max_sum:
            max_sum = sum(numbers[i:i+M])

        if sum(numbers[i:i+M]) < min_sum:
            min_sum = sum(numbers[i:i+M])

    print(f'#{z}', max_sum-min_sum)