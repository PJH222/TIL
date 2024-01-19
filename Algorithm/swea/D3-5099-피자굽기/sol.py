import sys
sys.stdin = open('./input.txt')

T = int(input())
for t in range(1,T+1):
    answer = 0
    N,M = list(map(int,input().split()))
    # 화덕에 들어가야할 모든 피자의 치즈 숫자
    c = list((map(int,input().split())))
    diction = {}
    j = 0
    for i in c:
        diction[j] = i
        j += 1
    else:
        j = 0
    x = 0 # 좌표
    oven = [0] * N
    number = [0] * N
    for i in range(len(oven)): #처음 oven의 빈칸 채우기
        oven[i] = diction[i]
        number[i] = i

    i = N - 1
        #여기서 사용한 i를 계속 사용 할 것임,,
    # print(diction)
    b = True
    while oven.count(0) != N: #oven 안까지 모든숫자가 0이되면 출력
        for j in range(N):
            if oven[j] != 0:
                oven[j] = oven[j]//2
                if oven[j] == 0 and i != M-1:
                    oven[j] = diction[i+1]
                    number[j] = i+1
                    i += 1
                    answer = number[j]
            # print(oven,number)
            if oven.count(0) == N-1:
                for k in range(N):
                    if oven[k] != 0:
                        answer = number[k]

    print('#{} {}'.format(t,answer+1))



            # if oven.count(0) == N:
            #     break
    for i in range(len(oven)):
        if oven[i] != 0:
            print('#{} {}'.format(t,number[i]))








# 대충 5번 돌면 치즈 살살 녹는다~
# cnt = 20
# for i in range(1,11):
#     # 대
#     cnt = cnt//2
#     print(cnt)