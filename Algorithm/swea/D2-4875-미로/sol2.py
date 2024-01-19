import sys
sys.stdin = open('input.txt')

# 4방향 위 아래 왼 오른 방향으로 0이 존재할 경우
# 각 경우에 대해 최 끝단 까지 움직여 3에 도달하는지 모두 확인 해야 함...

def dfs(maze, start, visited = []):
    visited.append(start)

    # for nod in maze[start]:

def boundary(x,y): #현재위치에서 이동가능한 위치
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    return True
            
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for t in range(int(input())):
    maze = []
    result = 0
    N = int(input())
    for i in range(N):
        a = list(input())
        maze.append(a)
        if '2' in a:
            x,y = a.index('2'), i
    # print(x,y)

    stack = [(y,x)]
    while stack:
        y,x = stack.pop()
        maze[y][x] = '1'
        for y_, x_ in move:
            dy = y_ + y
            dx = x_ + x
            if boundary(dx,dy) == False:
                continue
            if maze[dy][dx] == '3':
                result = 1
                break

            elif maze[dy][dx] == '0':
                stack.append((dy,dx))
                # print(stack)
        else:  # 브레이크 없이 끝나면 다음으로 진행
            continue
        break
    print(f'#{t+1} {result}')



