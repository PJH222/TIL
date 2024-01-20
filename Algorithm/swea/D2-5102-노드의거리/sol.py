import sys
sys.stdin = open('./input.txt')

# 푸는 방식은 맞는데, 시간초과 발생,,,
def find(stack):
    sub = [0,0]
    for i in range(len(stack)):
        for j in range(i+1,len(stack)):
            if i!=j and stack[i] != stack[j] and stack[i] != stack[j][::-1]:
                if stack[i][0] == stack[j][0] and (stack[j][-1] == S or stack[j][-1] == G or stack[i][-1] == S or stack[i][-1] == G):
                    sub = stack[j][::-1] + stack[i][1:]
                    stack.append(sub)

                elif stack[i][0] == stack[j][-1] and (stack[j][0] == S or stack[j][0] == G or stack[i][-1] == S or stack[i][-1] == G):
                    sub =stack[j][0:len(stack[j])-1] + stack[i]
                    # if sub not in stack:
                    stack.append(sub)

                elif stack[i][-1] == stack[j][0] and (stack[i][0] == S or stack[i][0] == G or stack[j][-1] == S or stack[j][-1] == G):
                    sub = stack[i] + stack[j][1:]
                    # if sub not in stack:
                    stack.append(sub)

                elif stack[i][-1] == stack[j][-1] and (stack[j][0] == S or stack[j][0] == G or stack[i][0] == S or stack[i][0] == G):
                    sub =stack[j][:len(stack[j])-1] + stack[i][::-1]
                    # if sub not in stack:
                    stack.append(sub)
                # print(stack[i], stack[j], sub, t)
                if (sub[0] == S and sub[-1] == G) or (sub[-1] == S and sub[0] == G):
                    # print(sub)
                    return len(sub) - 1
                # print(stack[i],stack[j], sub, t)


T = int(input())

for t in range(1, T+1):
    V,E = list(map(int,input().split()))
    stack = []
    result = []
    sub = []
    for i in range(E):
        one_node = list(map(int,input().split()))
        stack.append(one_node)
    S,G = list(map(int,input().split()))
    cnt = 0
    print('#{} {}'.format(t,find(stack)))








