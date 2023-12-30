# https://www.acmicpc.net/problem/1244

'''
예제 입력 1
8
0 1 0 1 0 0 0 1
2
1 3
2 3

예제 출력 1
1 0 0 0 1 1 0 1
'''

n = int(input())
lis_ = list(map(int,input().split()))
student = int(input())

for _ in range(student):
    gender , no = map(int,input().split())

    if gender == 1:
        aa = n//no
        if aa >= 1:
            for _ in range(aa):
                if 


