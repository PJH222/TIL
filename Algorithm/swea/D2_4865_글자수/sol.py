import sys
sys.stdin = open('./input.txt')

T = int(input())


for t in range(T):
    max = 0
    str1 = list(str(input()))
    str2 = list(str(input()))
    for i in str1:
        if i in str2 and str2.count(i) > max:
            max = str2.count(i)

    print(f'#{t+1}',max)
