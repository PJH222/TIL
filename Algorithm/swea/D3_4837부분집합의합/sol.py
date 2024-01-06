import sys
sys.stdin = open('./input.txt')

T = int(input())

for _ in range(T):
    nk = list(map(int,input().split()))
    n = nk[0]
    m = nk[1]
    nums = [1,2,3,4,5,6,7,8,9,10,11,12]
    result = []
    answer = 0
    sub_sum = 0
    aaa = []
    for i in range(12):
        result.append(0)


    for a in range(2):
        result[0] = a
        for b in range(2):
            result[1] = b
            for c in range(2):
                result[2] = c
                for d in range(2):
                    result[3] = d
                    for e in range(2):
                        result[4] = e
                        for f in range(2):
                            result[5] = f
                            for g in range(2):
                                result[6] = g
                                for h in range(2):
                                    result[7] = h
                                    for i in range(2):
                                        result[8] = i
                                        for j in range(2):
                                            result[9] = j
                                            for k in range(2):
                                                result[10] = k
                                                for l in range(2):
                                                    result[11] = l
                                                    if result.count(1) == n:
                                                        for z in range(12):
                                                            sub_sum += result[z]*nums[z]
                                                            # print(sub_sum)
                                                        if sub_sum == m:
                                                            answer += 1
                                                            sub_sum = 0
                                                        else:
                                                            sub_sum = 0

    print(f'#{_+1}',answer)
