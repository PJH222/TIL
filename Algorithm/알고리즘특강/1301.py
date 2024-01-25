## 함수
import random

def seqSearch(ary, fdata):
    pos = -1
    for i in range(len(ary)):
        if ary[i] == fdata:
            pos = i
            break
    return pos

## 변수


dataAry = [random.randint(30,190) for _ in range(20000000)]
findData = random.choice(dataAry)


## 메인
print('배열: ',dataAry)

position = seqSearch(dataAry,findData)
if position != -1:
    print(findData, '는',position,'위치에 있음.')
else:
    print(findData,'는 없어요 ㅠㅅㅠ')