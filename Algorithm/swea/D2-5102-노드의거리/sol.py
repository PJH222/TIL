import sys
sys.stdin = open('./input.txt')

def link(cnt,start):
    global list_start

    for i in go:
        if i[0] == start[0] and i not in list_start:
            list_start.append(i)
            cnt += 1
            start = i
            node.append(start+i[1])
        elif i[0] == start[1]:
            if (start+i[1])[0] == S and (start+i[1])[-1] == G :
                return cnt
            else:
                node.append(start + i[1])
                list_start.append(i)
                link(cnt,start)






T = int(input())
for t in range(1,T+1):
    node = []
    V,E = list(map(int,input().split()))
    for _ in range(E):
        go = list(map(int,input().split()))
        node.append(go)
    S,G = list(map(int,input().split()))
    min = 1000
    list_start = []
    cnt = 1
    start = [S,-1]
    if [S,G] in node or [G,S] in node:
        answer = 1
        break
    else:
        print(link(cnt,start))




