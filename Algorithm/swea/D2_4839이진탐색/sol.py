import sys
sys.stdin = open('./input.txt')

def binary(list,answer):
    result = 0
    start = 0
    end = len(list) - 1
    while start <= end: #결론적으로, start / middle / end는 index값
        middle = start + ((end-start)//2)
        if list[middle] == answer:
            return result

        elif list[middle] > answer:
            end = middle
            result += 1
        else:
            start = middle
            result += 1
    return 0

T = int(input())

for _ in range(T):
    lis = []
    pab = list(map(int,input().split())) #p는 전체 페이지 수, a , b는 각각 찾아야 하는 페이지 수
    p,a,b = pab[0], pab[1], pab[2]

    for i in range(1,p+1):
        lis.append(i)

    if binary(lis,a) > binary(lis,b):
        print(f'#{_+1}',"B")
    elif binary(lis,a) < binary(lis,b):
        print(f'#{_ + 1}', "A")
    else:
        print(f'#{_ + 1}', 0)
    # print(lis)


