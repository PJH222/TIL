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
    route = []
    cnt = 0

    for _ in range(e): #횟수만 중요한 것이라 _로 표시, 도착 정보가 없어서 append 하는 방법 밖에 없을 듯...
        ss = list(map(int, input().split()))
        nods.append(ss)

    route = list(map(int, input().split()))

    # print(nods)
    while cnt <= v:
        for i in nods:
            for j in nods:
                if i != j and i[1] == j[0]:
                    path = [i[0],j[1]]
                    if path not in nods:
                        nods.append(path)
                    if path == route:
                        cnt += 1000
                    # print(path, route)
        cnt += 1
    # print(cnt, v)
    if cnt > v + 2:
        print('#{} {}'.format(t + 1, 1))
    else:
        print('#{} {}'.format(t + 1, 0))


