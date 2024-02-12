def bfs(i,j,reset_maps):
    global stack

    if i < 0 or j < 0 or i >= len(reset_maps) or j >= len(reset_maps[0]) or reset_maps[i][j] == "X":
        return

    if reset_maps[i][j] != "X":
        stack += int(reset_maps[i][j])
        reset_maps[i][j] = "X"

    # print(reset_maps)
    # for k in reset_maps:
    #     print(k)
    # print()
    bfs(i+1,j,reset_maps)
    bfs(i, j+1, reset_maps)
    bfs(i-1,j,reset_maps)
    bfs(i,j-1,reset_maps)

def solution(maps):
    global stack
    answer = []
    reset_maps = []

    for i in maps:
        reset_maps.append(list(i))

    # print(reset_maps)
    for i in range(len(reset_maps)):
        for j in range(len(reset_maps[0])):
            stack = 0
            bfs(i,j,reset_maps)
            if stack != 0:
                answer.append(stack)


    # print(reset_maps)
    # print(len(answer))


    return sorted(answer) if len(answer) > 0 else [-1]

print(solution(["X591X",
                "X1X5X",
                "X231X",
                "1XXX1"]	))
print(solution(["XXX","XXX","XXX"]	))
print(solution(["1X3","X2X","1X3"]	))
print(solution(["1X3","XXX","1X3"]	))
print(solution(["1X3X",
                "XXXX",
                "X1X3"]	))