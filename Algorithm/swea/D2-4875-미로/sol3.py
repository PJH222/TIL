import sys
sys.stdin = open('input.txt')

def bfs(maze,x,y):
    global indict
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze) or maze[y][x] == "1":
        return

    if maze[y][x] == "2":
        # print("시발 잘 맞자너 왜 안됨??")
        indict = True
        return
    else:
        maze[y][x] = "1"

    # for i in maze:
    #     print(i)
    # else:
    #     print()

    bfs(maze, x + 1, y)
    bfs(maze, x - 1, y)
    bfs(maze, x, y + 1)
    bfs(maze, x, y - 1)
    return


for t in range(int(input())):

    indict = False
    maze = []
    result = 0
    N = int(input())
    for i in range(N):
        a = list(input())
        maze.append(a)
        if '2' in a:
            x,y = a.index('2'), i


    for yy in range(len(maze)):
        for xx in range(len(maze)):
            if maze[yy][xx] == "3":
                bfs(maze,xx,yy)
                # print(indict)
                # print(indict)
                if indict == True:
                    print("#{} {}".format(t + 1,1))
                else:
                    print("#{} {}".format(t + 1, 0))
                # print(indict)

    # print(1)