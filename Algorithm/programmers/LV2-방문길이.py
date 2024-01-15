# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0

    x ,y = 0,0 #현재 위치 (x,y)
    indict = ''
    new_dirs = [[0,0]]
    answer_route = []
    all_route = []
    stack = []
    for i in dirs:
        [x,y,indict] = play([x,y,i])
        xy = [x,y]
        new_dirs.append(xy)
        # print(xy)

    for i in range(len(new_dirs)-1):
        if new_dirs[i] != new_dirs[i+1]:
            all_route.append(new_dirs[i:i+2])
    # print(all_route)
    answer = len(all_route)
    # print(all_route)

    for i in range(len(all_route)):
        for j in range(2):
            if j == 0:
                if all_route.count(all_route[i]) >= 1 and all_route[i] not in stack:
                    cnt = all_route.count(all_route[i]) - 1
                    stack.append(all_route[i])
                    stack.append(all_route[i][::-1])
                    # print(stack)
                    for _ in range(cnt):
                        answer -= 1
                        # print(1)
                    if all_route[i][::-1] in all_route:
                        cnt = all_route.count(all_route[i][::-1])
                        for _ in range(cnt):
                            answer -= 1

    # print(stack)


    return answer

def play(list):
    x = list[0]
    y = list[1]
    indic = list[2]
    if indic == "U" and y != 5:
        y += 1
    elif indic == "D" and y != -5:
        y -= 1
    elif indic == "R" and x != 5:
        x += 1
    elif indic == "L" and x != -5:
        x -= 1

    result = [x,y,indic]

    return result

print(solution("ULURRDLLU"	))
print(solution("LULLLLLLU"	))
print(solution("LRLRLRLRL"	))