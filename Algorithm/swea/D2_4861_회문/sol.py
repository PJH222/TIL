import sys
sys.stdin = open('./input.txt')

T = int(input())


for t in range(T):
    nm = list(map(int,input().split()))
    n = nm[0]
    m = nm[1]
    str_table = []
    answer = ''
    for _ in range(n):
        str_table.append(list(str(input())))

    #가로방향 탐색
    for i in str_table:
        for x in range(len(i)-m+1):
            for idx in range(x,x+m//2):
                # print(t,i[x+idx],i[x+m - idx-1])
                if i[x+idx] == i[x+m - idx - 1]:
                    if idx == x+m//2 - 1:
                        answer = ''.join(i[x:x+m])
                        break
                    else:
                        continue
                else:
                    break

    #세로방향 탐색


    print(answer)
