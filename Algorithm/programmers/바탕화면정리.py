# https://school.programmers.co.kr/learn/courses/30/lessons/161990
def solution(wallpaper):
    answer = []
    result_dx = ['.'] * len(wallpaper[0])
    result_dy = ['.'] * len(wallpaper)

    if wallpaper == ["#"]:
        print(wallpaper)
        return [0,0,1,1]
    #x축 위로 생기는 그림자
    x_end = 0
    x_start = 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if result_dx[j] != list(wallpaper[i])[j]:
                result_dx[j] = "#"

    #사이에 . 있는 부분 #으로 바꿔주기
    for i in range(len(result_dx)):
        if result_dx[i] == "#":
            x_start = i
            break

    for i in range(len(result_dx)-1,0,-1):
        if result_dx[i] == "#":
            x_end = i
            break

    for i in range(x_start,x_end+1):
        result_dx[i] = "#"




    # y축 위로 생기는 그림자
    y_end = 0
    y_start = 0

    for i in range(len(wallpaper[0])):
        for j in range(len(wallpaper)):
            if result_dy[j] != list(wallpaper[j])[i]:
                result_dy[j] = "#"

    # 사이에 . 있는 부분 #으로 바꿔주기
    for i in range(len(result_dy)):
        if result_dy[i] == "#":
            y_start = i
            break

    for i in range(len(result_dy)-1,0,-1):
        if result_dy[i] == "#":
            y_end = i
            break

    for i in range(y_start,y_end+1):
        result_dy[i] = "#"

    #시작점 y 값
    for y in result_dy:
        if y == '#':
            answer.append(result_dy.index(y))
            break

    # 시작점 x 값
    for x in result_dx:
        if x == '#':
            answer.append(result_dx.index(x))
            break

    # 마지막점 y값
    for i in range(len(result_dy)):
        if i == 0 and len(result_dy) == 1:
            answer.append(i+1)
            break
        elif i == 0:
            continue
        elif result_dy[i] == "." and result_dy[i-1] == "#":
            answer.append(i)
            break
        elif i == len(result_dy) - 1:
            answer.append(i+1)
            break

    # 마지막점 x값
    for i in range(len(result_dx)):
        if i == 0 and len(result_dx) == 1:
            answer.append(i+1)
            break
        elif i == 0:
            continue
        elif result_dx[i] == "." and result_dx[i-1] == "#":
            answer.append(i)
            break
        elif i == len(result_dx) - 1:
            answer.append(i+1)
            break
    # print(result_dx, result_dy)


    print(result_dx,result_dy)
    return answer

# print(solution([".#...", "..#..", "...#."]	))
# print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]	))
# print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]	))
# print(solution(["..", "#."]	))
# print(solution(["#.", "#."]	))
# print(solution(["#.", ".."]	))
# print(solution(["#"]	))
# print(solution(["###","###","###"]))
# print(solution(["#####","#####","#####"]))
# print(solution(["#...#","..###","..#.."]))
# print(solution(["#...#",".....","....."]))
# print(solution(["#....",".....","#...."]))
# print(solution(["...","###","..."]))
# print(solution(["...",".#.","..."]))
print(solution(["..#"]))
print(solution(["#.#"]))
print(solution(["#",".","."]))
print(solution(["#",".","#"]))
