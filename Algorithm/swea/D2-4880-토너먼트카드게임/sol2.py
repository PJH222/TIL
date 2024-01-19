import sys
sys.stdin = open('./input.txt')

def rsp(a): #rock scissor paper!
    a1 ,a2 = a[0],a[1]

    if a1[1] == 1 and a2[1] == 2:
        return a2
    if a1[1] == 1 and a2[1] == 3:
        return a1
    if a1[1] == 2 and a2[1] == 1:
        return a1
    if a1[1] == 2 and a2[1] == 3:
        return a2
    if a1[1] == 2 and a2[1] == 1:
        return a1
    if a1[1] == 2 and a2[1] == 3:
        return a2
    if a1[1] == 3 and a2[1] == 1:
        return a2
    if a1[1] == 3 and a2[1] == 2:
        return a1
    if (a1[1] == 1 and a2[1] == 1) or ( a1[1] == 2 and a2[1] == 2) or ( a1[1] == 3 and a2[1] == 3):
        return a1 if a1 < a2 else a2

def play(cards):
    stack = []
    new_list = []
    if len(cards) > 1:
        for number, card in cards:
            stack.append((number, card))
            if len(stack) == 2:
                new_list.append(rsp(stack))
                stack = []
        else:
            if len(stack) == 1:
                new_list.append(stack[0])
    else:
        return cards[0][0] + 1
    return play(new_list)


T = int(input())
for t in range(T):
    N = int(input())
    cards = list(map(int,input().split()))
    new_list = []
    for number,card in enumerate(cards):
        new_list.append((number,card))
    print('#{} {}'.format(t+1,play(new_list)))
