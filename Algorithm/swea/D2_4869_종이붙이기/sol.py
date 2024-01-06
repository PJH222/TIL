import sys
sys.stdin = open('./input.txt')

T = int(input())

# 3 = 1+1+1 / 1+2 / 2+1 >> 1,2로 조합하여 구하고 난 이후에, 2들어간 것은 *2로 답을 구하면 될 것 같다..
#   = 3c0 + 2C1*2
    # 4 = 1 1 1 1 / 2 1 1 / 1 2 1 / 1 1 2 / 2 2
    #   = 4c0 + 3c1*2**1 + 2c2*2**2 (**n에서 n은 2의 갯수)
    #   = 1 + (2 + 2 + 2) + 4
    # 5 = 1 1 1 1 1 / 1 1 1 2 / 1 1 2 1 / 1 2 1 1 / 2 1 1 1 / 1 2 2 / 2 1 2 / 2 2 1
    #   = 1 + (2 + 2 + 2 + 2) + (4 + 4 + 4)
    #   = 5c0 + 4c1*2**1 + 3c2*2**2
    # 6 = 6c0 + 5c1*2 + 4c2*4 + 3c3*8
    #   = 1 + 10 + 24 + 8
    #   = 43
for t in range(T):
    answer = []
    ans_sum = 0
    n = int(input())
    for i in range(n+1): #1의 갯수
        for j in range(n//2+1): #2의 갯수
            if i + 2*j == n//10:
                answer = [i,j] #1의 갯수와 2의 갯수를 표시
                if j == 0:
                    ans_sum += 1
                elif i == 0:
                    ans_sum += 2**j
                else:
                    combi = 0
                    a = i + j
                    b = 1 #팩토리얼
                    c = 1 #나눠주는 값
                    # print(t+1,i,j)
                    for k in range(i+1,i+j+1):      #4c2 = 4*3 / 2*1
                        b *= k                  #5c3 = 5*4*3/3*2*1
                    for l in range(1,j+1):
                        c *= l

                    ans_sum += (b//(c))*2**j
                    # print(b//c)

    print(f'#{t+1}',ans_sum)




