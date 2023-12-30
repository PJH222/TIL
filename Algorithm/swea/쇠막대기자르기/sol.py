# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl47b6DGMDFAXm&categoryId=AWVl47b6DGMDFAXm&categoryType=CODE&problemTitle=%EB%A7%89%EB%8C%80&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
import sys
sys.stdin = open('./input.txt')

T = int(input())

for _ in range(T):
    answer = 0
    nums = 0
    lob = str(input().split())
    for i in range(2,len(lob)-2):
        if (lob[i-1] == '(' and lob[i] == '('):
            nums += 1

        elif lob[i-1] == '(' and lob[i] == ')':
            answer += nums
            #print('추가')
        elif lob[i-1] == ')' and lob[i] == ')':
            nums -= 1
            answer += 1

        #print(lob[i])
        #print(nums)
    print(f'#{_+1} {answer}')
