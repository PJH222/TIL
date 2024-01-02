# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    save = []
    
    indict = 4 #초기화
    if ext == "code":
        indict = 0
    elif ext == "date":
        indict = 1
    elif ext == "maximum":
        indict = 2
    elif ext == "remain":
        indict = 3

    if indict == 0:
        for i in data:
            if i[indict] < val_ext:
                save.append(i[0])
                save.append(i[1])
                save.append(i[2])
                save.append(i[3])
                answer.append(save)
                save = []

    elif indict == 1:
        for i in data:
            if i[indict] < val_ext:
                save.append(i[0])
                save.append(i[1])
                save.append(i[2])
                save.append(i[3])
                answer.append(save)
                save = []

    elif indict == 2:
        for i in data:
            if i[indict] < val_ext:
                save.append(i[0])
                save.append(i[1])
                save.append(i[2])
                save.append(i[3])
                answer.append(save)
                save = []

    elif indict == 3:
        for i in data:
            if i[indict] < val_ext:
                save.append(i[0])
                save.append(i[1])
                save.append(i[2])
                save.append(i[3])
                answer.append(save)
                save = []

    del answer[0]

    if sort_by == "code":
        indict = 0
    elif sort_by == "date":
        indict = 1
    elif sort_by == "maximum":
        indict = 2
    else:
        indict = 3

    answer.sort(key=lambda x: x[indict])

    # del answer[0]

    return answer



print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]	, "date",20300501,	"remain"	))