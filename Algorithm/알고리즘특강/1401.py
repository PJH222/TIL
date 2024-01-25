## 함수

def openBox():
    global cnt
    print('상자열기~~')
    cnt -= 1
    if cnt == 0:
        print('*** 선물 넣기 ***')
        return
    openBox()
    print('상자닫기##')


cnt = 3
openBox()