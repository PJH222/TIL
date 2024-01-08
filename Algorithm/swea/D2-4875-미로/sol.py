import sys
sys.stdin = open('input.txt')

# 4방향 위 아래 왼 오른 방향으로 0이 존재할 경우
# 각 경우에 대해 최 끝단 까지 움직여 3에 도달하는지 모두 확인 해야 함...

def waymore(cage,y,x): #움질일 수 있는 방향 찾기
    way = []
    if 0 < y < len(sen) - 1 and 0 < x < len(sen) - 1:
        if cage[y+1][x] == '0':
            way.append([y+1,x])
        if cage[y-1][x] == '0':
            way.append([y-1,x])
        if cage[y][x+1] == '0':
            way.append([y,x+1])
        if cage[y][x-1] == '0':
            way.append([y,x-1])

    elif y == 0 and 0 < x < len(sen) - 1:
        if cage[y + 1][x] == '0':
            way.append([y + 1, x])
        if cage[y][x + 1] == '0':
            way.append([y, x + 1])
        if cage[y][x - 1] == '0':
            way.append([y, x - 1])

    elif y == len(sen) - 1 and 0 < x < len(sen) - 1:
        if cage[y - 1][x] == '0':
            way.append([y - 1, x])
        if cage[y][x + 1] == '0':
            way.append([y, x + 1])
        if cage[y][x - 1] == '0':
            way.append([y, x - 1])

    elif x == 0 and 0 < y < len(sen) - 1:
        if cage[y + 1][x] == '0':
            way.append([y + 1, x])
        if cage[y - 1][x] == '0':
            way.append([y - 1, x])
        if cage[y][x + 1] == '0':
            way.append([y, x + 1])

    elif x == len(sen) - 1 and 0 < y < len(sen) - 1:
        if cage[y + 1][x] == '0':
            way.append([y + 1, x])
        if cage[y - 1][x] == '0':
            way.append([y - 1, x])
        if cage[y][x - 1] == '0':
            way.append([y, x - 1])

    elif x == 0 and y == 0:
        if cage[y + 1][x] == '0':
            way.append([y + 1, x])
        if cage[y][x + 1] == '0':
            way.append([y, x + 1])

    elif x == 0 and y == len(sen) - 1:
        if cage[y - 1][x] == '0':
            way.append([y - 1, x])
        if cage[y][x + 1] == '0':
            way.append([y, x + 1])

    elif x == len(sen) - 1 and y == 0:
        if cage[y + 1][x] == '0':
            way.append([y + 1, x])
        if cage[y][x - 1] == '0':
            way.append([y, x - 1])

    elif x == len(sen) - 1 and y == len(sen) - 1:
        if cage[y - 1][x] == '0':
            way.append([y - 1, x])
        if cage[y][x - 1] == '0':
            way.append([y, x - 1])

    return way

T = int(input())


for t in range(T):
    cage = []
    cnt = 0 #0의 갯수를 세어주기 위한 변수
    direct = '' #up down left right 중 하나, 현재 위치로 들어올 때의 방향을 의미
    xy0 = [0,0] #처음 시작점
    xy1 = [0,0] #현재 위치
    xy2 = [0,0] #도착 지점
    xy_except = [] #분기점
    length = 0 #총 이동한 거리


    for i in range(int(input())):
        sen = list(map(str, input()))
        cage.append(sen)
        if '0' in sen:
            cnt += sen.count('0')
        if '2' in sen:
            xy0 = [i,sen.index('2')]
            xy1 = [i, sen.index('2')]
            y = xy1[0]
            x = xy1[1]
        if '3' in sen:
            xy2 = [i, sen.index('3')]
    print(waymore(cage,y,x))
    for i in range(cnt):
        if len(waymore(cage,y,x)) == 1:
            y,x = waymore(cage,y,x)
            print(y,x)
        # else:
            # print(len(waymore(cage,y,x)))





