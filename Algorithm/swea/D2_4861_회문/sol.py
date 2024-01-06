import sys
sys.stdin = open('./input.txt')

T = int(input())


for t in range(T):
    nm = list(map(int,input().split()))
    n = nm[0]
    m = nm[1]
    str_table = [] #기본 테이블
    yx_table = [] # yx 변환 테이블
    answer = ''
    
    #2차원 테이블 만들기
    for _ in range(n):
        a = list(str(input()))
        str_table.append(a)

    yx_table = [[0]*n for i in range(n)]

    #가로방향 탐색
    for i in str_table:
        for x in range(len(i)-m+1):
            for idx in range(x,int(x+m//2)):
                # print(t,i[x+idx],i[x+m - idx-1])
                if i[x+idx] == i[x+m - idx - 1]:
                    if idx == x+m//2 - 1:
                        answer = ''.join(i[x:x+m])
                        break
                    else:
                        continue
                else:
                    break
    # print(str_table)
    if len(answer) == m:
        print(f'#{t + 1}', answer)
        continue #가로탐색에서 끝나면 다음 input 받기


    ##xy >> yx 테이블 변환
    for y_idx in range(n):
        for x_idx in range(n):
            yx_table[y_idx][x_idx] = str_table[x_idx][y_idx]

    #세로방향 탐색
    for i in yx_table:
        for y in range(len(i) - m + 1):
            for idx in range(y, int(y + m // 2)):
                # print(t+1,i[x+idx],i[x+m - idx-1])
                if i[y + idx] == i[y + m - idx - 1]:
                    # print(i[y + idx], i[y + m - idx - 1])
                    if idx == y + m // 2 - 1:
                        answer = ''.join(i[y:y + m])
                        break
                    else:
                        continue
                else:
                    break

    # print(yx_table)
    # print(str_table)

    print(f'#{t+1}',answer)
