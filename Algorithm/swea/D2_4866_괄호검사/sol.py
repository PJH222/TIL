import sys
sys.stdin = open('./input.txt')

T = int(input())
sum1 = ['{','}']
sum2 = ['(',')']



for t in range(T):
    a = list(map(str,input().split()))
    stack = [0]

    for i in a:
        for j in (range(len(i))):
            if i[j] in sum1:
                if (i[j] == sum1[1] and stack[-1] == sum1[0]):
                    stack.pop()
                else:
                    stack.append(i[j])
                # print(stack)

            elif i[j] in sum2:
                if (i[j] == sum2[1] and stack[-1] == sum2[0]):
                    stack.pop()
                else:
                    stack.append(i[j])
                # print(stack)

        # print(stack)
    if len(stack) == 1:
        print('#{} {}'.format(t+1,1))
    else:
        print('#{} {}'.format(t + 1, 0))


