import sys
sys.stdin = open('input.txt')

T = int(input())


for t in range(T):
    s = list(str(input()))
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        elif s[i] == stack[-1]:
            stack.pop()
        elif s[i] != stack[-1]:
            stack.append(s[i])
    print('#{} {}'.format(t+1,len(stack)))




