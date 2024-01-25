## 함수
import random

def binSearch(ary,fdata):
    global cnt
    pos = -1
    start = 0
    end = len(ary) - 1
    while start <= end :
        cnt += 1
        mid = (start + end) // 2
        if ary[mid] == fdata:
            pos = mid
            break
        elif ary[mid] < fdata:
            start = mid + 1
        elif ary[mid] > fdata:
            end = mid - 1

    return pos


## 변수


dataAry = [random.randint(300000,1900000) for _ in range(1000000)]
dataAry.sort()
findData = random.choice(dataAry)


## 메인
cnt = 0
print('배열: ',dataAry)

position = binSearch(dataAry,findData)
if position != -1:
    print(findData, '는',position,'위치에 있음.',cnt,'번 세어 구했씁니다 ㅎㅅㅎ')
else:
    print(findData,'는 없어요 ㅠㅅㅠ')