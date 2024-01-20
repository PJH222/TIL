import sys
sys.stdin = open('./input.txt')

def find(stack):
    sub = []
    cnt = 0
    # print(S,G)
    for i in range(len(stack)):
        # print(stack)
        if stack[i][0] == S or stack[i][0] == G or stack[i][-1] == S or stack[i][-1] == G: # 일단 출발할 수 있으면 계산
            for j in range(len(stack)):
                if stack[i] != stack[j] and stack[i][::-1] != stack[j]: # 같은게 아닐 경우만 계산
                    if stack[i][0] == S and stack[j][0] == stack[i][-1]:
                        sub = stack[i] + stack[j][1:]
                        if (sub[0] == S and sub[-1] == G) or (sub[0] == G and sub[-1] == S):
                            return len(sub) - 1
                        stack.append(sub)

                    elif stack[i][0] == S and stack[j][-1] == stack[i][-1]:
                        sub = stack[i] + stack[j][::-1][1:]
                        if (sub[0] == S and sub[-1] == G) or (sub[0] == G and sub[-1] == S):
                            return len(sub) - 1
                        stack.append(sub)

                    elif stack[i][0] == G and stack[j][0] == stack[i][-1]:
                        sub = stack[i] + stack[j][1:]
                        if (sub[0] == S and sub[-1] == G) or (sub[0] == G and sub[-1] == S):
                            return len(sub) - 1
                        stack.append(sub)

                    elif stack[i][0] == G and stack[j][-1] == stack[i][-1]:
                        sub = stack[i] + stack[j][::-1][1:]
                        if (sub[0] == S and sub[-1] == G) or (sub[0] == G and sub[-1] == S):
                            return len(sub) - 1
                        stack.append(sub)

                    # 어느 정도 완성

                    elif stack[i][-1] == S and stack[j][-1] == stack[i][0]:
                        sub = stack[j] + stack[i][1:]
                        if (sub[0] == S and sub[-1] == G) or (sub[0] == G and sub[-1] == S):
                            return len(sub) - 1
                        stack.append(sub)

                    elif stack[i][-1] == G and stack[j][-1] == stack[i][0]:
                        sub = stack[j] + stack[i][1:]
                        if (sub[0] == S and sub[-1] == G) or (sub[0] == G and sub[-1] == S):
                            return len(sub) - 1
                        stack.append(sub)

                    elif stack[i][-1] == S and stack[j][::-1][-1] == stack[i][0]:
                        sub = stack[j][::-1] + stack[i][1:]
                        if (sub[0] == S and sub[-1] == G) or (sub[0] == G and sub[-1] == S):
                            return len(sub) - 1
                        stack.append(sub)

                    elif stack[i][-1] == G and stack[j][::-1][-1] == stack[i][0]:
                        sub = stack[j][::-1] + stack[i][1:]
                        if (sub[0] == S and sub[-1] == G) or (sub[0] == G and sub[-1] == S):
                            return len(sub) - 1
                        stack.append(sub)

    return find(stack)

T = int(input())

for t in range(1, T+1):
    V,E = list(map(int,input().split()))
    stack = []
    result = []
    sub = []

    stack = [list(map(int,input().split())) for i in range(E)]
    S, G = list(map(int, input().split()))
    if [S,G] in stack or [G,S] in stack:
        print('#{} {}'.format(t,1))
        continue
    print('#{} {}'.format(t,find(stack)))

