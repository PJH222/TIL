import sys
sys.stdin = open('input.txt')

#이 문제의 핵심은, `경로 자체를 표시하라` 가 아니라 `되는지 안되는지 확인하라` 이다,,,

T = int(input())
node = []

for t in range(T):
    ve = list(map(int,input().split()))
    v = ve[0]
    e = ve[1]
    nods = []
    answer = []
    path = [0,0]
    all_path = []

    for _ in range(e): #횟수만 중요한 것이라 _로 표시, 도착 정보가 없어서 append 하는 방법 밖에 없을 듯...
        ss = list(map(int, input().split()))
        nods.append(ss)

    cnt = 0

    while cnt != v:     #어차피 v를 넘어버리면 아무 의미가 없음...
        for i in nods: #뒤에 꺼
            for j in nods: #앞에 꺼
                if i != j and i[0] == j[1]:
                    path = [j[0],i[1]]
                    if path not in nods:
                        nods.append(path)
        cnt += 1

    for _ in range(1):
        arrive_where = list(map(int, input().split()))
        a = arrive_where[0] #출발점
        z = arrive_where[1] #도착점
        if [a,z] in nods:
            print('#{} {}'.format(t+1,1))
        else:
            print('#{} {}'.format(t + 1, 0))








