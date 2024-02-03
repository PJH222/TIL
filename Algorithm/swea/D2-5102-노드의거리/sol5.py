import sys
sys.stdin = open('./input.txt')


def go_inside(visited, all_route, position, stack,minn):
    if len(all_route) == 0:
        stack = []
        return
    # print("들어간다~~")
    if visited[S - 1] == 1 and visited[G - 1] == 1:
        print(23232414124,visited,stack)
        if minn > len(stack):
            minn = len(stack)
        return

    for i in all_route[position]:
        if visited[i - 1] == 0:
            visited[i - 1] = 1
            stack.append(i)
            position = stack[-1]
            return go_inside(visited, all_route, position, stack, minn)
    else:
        if visited[G - 1] != 1:
            a = stack.pop()
            visited[a - 1] = 0 # 직전의 위치에서 visited를 0 으로 바꾸기
            position = stack[-1]    # 직전의 위치로 돌아가기
            all_route[position].remove(a)   # 갈 필요 없는 위치는 지우기
            if len(all_route[position]) == 0:
                del all_route[position]
            print(visited)
            # visited[stack.pop() - 1] = 0
            # position = stack[-1]
            print(stack)

            return go_inside(visited, all_route, position, stack, minn)   #안되면 다시 처음부터

        else:
            # print("진짜 마지막")
            # print(stack)
            return
    # if visited[G - 1] != 1:
    #     before = stack.pop()
    #     del all_route[before]
    #     return go_inside(visited, all_route, position, stack)




        # 갈곳 없는 상황에서
        # 어떻게 되돌아가지???
        # else:
        #     print("자 다시 드가자~")
        #     continue


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    g = [[] for _ in range(V+1)]
    visited = [0] * V

    all_route = {}
    minn = V + 1
    for _ in range(E):
        i, j = map(int, input().split())
        if i not in all_route and j not in all_route:
            all_route[i] = [j]
            all_route[j] = [i]

        elif i not in all_route:
            all_route[i] = [j]
            all_route[j].append(i)

        elif j not in all_route:
            all_route[j] = [i]
            all_route[i].append(j)

        else:
            all_route[i].append(j)
            all_route[j].append(i)


    S, G = map(int, input().split())
    visited[S-1] = 1
    position = S # 현재 위치

    print(all_route)
    # print(visited)
    stack = []
    go_inside(visited,all_route,position, stack, minn)
    print(all_route)
    print("#{} {}".format(tc,len(stack)))



