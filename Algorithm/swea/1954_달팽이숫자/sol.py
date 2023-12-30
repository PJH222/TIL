import sys
sys.stdin = open('./input.txt')

T = int(input())


indic = 'R'
x = 0
y = 0

for i in range(T):
    n = int(input())
    answer = [['_' for i in range(n)] for i in range(n)]
    #print(answer)
    for k in range(n*n):
        if indic == 'R':
            answer[y][x] = str(k+1)
            if x+1 < n and answer[y][x+1] == '_':
                x += 1
            else:
                indic = 'D'
                y += 1

        elif indic == 'D':
            answer[y][x] = str(k+1)
            if y + 1 < n and answer[y+1][x] == '_':
                y += 1
            else:
                indic = 'L'
                x -= 1

        elif indic == 'L':
            answer[y][x] = str(k+1)
            if x > 0 and answer[y][x-1] == '_':
                x -= 1
            else:
                indic = 'U'
                y -= 1

        else:
            answer[y][x] = str(k+1)
            if y > 0 and answer[y-1][x] == '_':
                y -= 1
            else:
                indic = 'R'
                x += 1
    indic = 'R'
    x = 0
    y = 0
    print(f'#{i+1}')
    for j in answer:
        print(' '.join(j))
