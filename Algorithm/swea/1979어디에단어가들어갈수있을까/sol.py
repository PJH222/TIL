import sys
sys.stdin = open('./input.txt')


T = int(input())

for _ in range(T):
    answer = 0
    table = []
    cnt = 0
    N, K = map(int,input().split())

    for o in range(N):
        a = list(map(str,input().split()))

        a.append('-')   #최후 식별자
        a.insert(0,'-') #최선 식별자
        b = ''.join(a)

        c = '-'+ '1' * K + '0' #케이스는 3가지 경우 밖에 없음
        d = '0'+ '1' * K + '-'
        e = '0' + '1' * K + '0' #얘가 제대로 안세어짐.. 111011101110111 인 경우 01110이 두번만 세어짐.. 왜그런거지??

        #print(b)
        if c in b:
            cnt = b.count(c)
            answer += cnt
        if d in b:
            cnt = b.count(d)
            answer += cnt
        if e in b:
            cnt = b.count(e)
            answer += cnt


        for i in range(2):
            a.remove('-')
        table.append(a)
    #print(table)
    t_table = [[0 for l in range(N)] for l in range(N)] #행열 => 열행으로 변환하기 위한 디폴트 테이블
    
    for y in range(N):
        for x in range(N):
            t_table[x][y] = table[y][x]
    #print(t_table)

    for y in t_table:
        y.insert(0,'-')
        y.append('-')
        g = ''.join(y)

        if c in g:
            cnt = g.count(c)
            answer += cnt
        if d in g:
            cnt = g.count(d)
            answer += cnt
        if e in g:
            cnt = g.count(e)
            answer += cnt
    print(f'#{_+1} {answer}')
    #print(c,d,e)















