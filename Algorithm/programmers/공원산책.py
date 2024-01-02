# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    answer = [] #y,x 로 나오게끔...
    x = 0 #초기화
    y = 0 #초기화
    num = 1 #현재 이동한 거리
    lim = 0 #최대 이동 거리수
    # print(park[0][1],park[0]) #굳이 리스트로 만들 필요 없음.
    # print(routes[0][2])

    for i in range(len(park)): # y길이
        for j in range(len(park[0])): #x길이
            if park[i][j] == "S":
                y,x = i,j
                break


    for i in routes:
        for num in range(1,int(i[2])+1):
            if i[0] == "E":
                if x + int(i[2]) + 1 > len(park[0]): #밖으로 나가게 되면 break
                    # print(i[0],1)
                    break

                if park[y][x+num] == "X": #X를 만나면 break
                    # print(i[0],2)
                    break

                elif num == int(i[2]) and park[y][x + num] != "X": #최종 이동거리에서 O라면, x위치 변환
                    x += num #x축 현재위치 이동
                    # print(i[0],4)

            elif i[0] == "S":
                if y + int(i[2]) + 1 > len(park[0]):  # 밖으로 나가게 되면 break
                    # print(i[0], 1)
                    break

                if park[y+num][x] == "X":  # X를 만나면 break
                    # print(i[0], 2)
                    break

                elif num == int(i[2]) and park[y+num][x] != "X":  # 최종 이동거리에서 O라면, x위치 변환
                    y += num  # x축 현재위치 이동
                    # print(i[0], 4)


            elif i[0] == "W":
                if x - int(i[2]) + 1 < 1:  # 밖으로 나가게 되면 break
                    # print(i[0], 1)
                    break

                if park[y][x-num] == "X":  # X를 만나면 break
                    # print(i[0], 2)
                    break

                elif num == int(i[2]) and park[y][x-num] != "X":
                    # 최종 이동거리에서 O라면, x위치 변환
                    x -= num  # x축 현재위치 이동
                    # print(i[0], 4)

            elif i[0] == "N":
                if y - int(i[2]) + 1 < 1:  # 밖으로 나가게 되면 break
                    # print(i[0], 1)
                    break

                if park[y - num][x] == "X":  # X를 만나면 break
                    # print(i[0], 2)
                    break

                elif num == int(i[2]) and park[y - num][x] != "X":  # 최종 이동거리에서 O라면, x위치 변환
                    y -= num  # x축 현재위치 이동
                    # print(i[0], 4)

    answer.append(y)
    answer.append(x)

    return answer




print(solution(["SOO","OOO","OOO"]	,["E 2","S 2","W 1"]	)) #[2,1]
print(solution(["SOO","OXX","OOO"]	,["E 2","S 2","W 1"]	)) #[0,1]
print(solution(["OSO","OOO","OXO","OOO"]	,["E 2","S 3","W 1"]	)) #[0,0]