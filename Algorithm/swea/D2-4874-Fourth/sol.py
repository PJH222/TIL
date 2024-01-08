import sys
sys.stdin = open('input.txt')

def fourth(inputlist):
    answer = 0
    stack = []
    indict = True
    for i in inputlist:
        if i.isdigit():
            stack.append(int(i))
        else:
            if i == '+':
                if len(stack) < 2:
                    indict = False
                else:
                    answer = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(answer)

            elif i == '-':
                if len(stack) < 2:
                    indict = False
                else:
                    answer = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(answer)

            elif i == '*':
                if len(stack) < 2:
                    indict = False
                else:
                    answer = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(answer)

            elif i == '/':
                if len(stack) < 2:
                    indict = False
                else:
                    answer = stack[-2] // stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(answer)

            elif i == '.':
                if len(stack) == 1:
                    return print('#{} {}'.format(t + 1, stack[0]))
                else:
                    indict = False

            if indict == False:
                return print('#{} error'.format(t + 1))

    # return print('#{} {}'.format(t + 1,stack[0]))



T = int(input())


for t in range(T):
    a = list(map(str,input().split()))
    fourth(a)
