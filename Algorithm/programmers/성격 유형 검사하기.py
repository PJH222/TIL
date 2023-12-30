# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    answer = ''
    score = []
    mbti = ['RT','TR','CF','FC','JM','MJ','AN','NA']
    mbti_score = [0,0,0,0,0,0,0,0]
    for i in choices:
        score.append(i-4)

    for i in range(len(survey)):
        a = survey[i]
        b = mbti.index(a)
        mbti_score[b] += score[i]

    print(mbti_score)

    if mbti_score[0]-mbti_score[1] >0:
        answer += "T"
    elif mbti_score[0]-mbti_score[1] <0:
        answer += "R"
    else:
        answer += "R"

    if mbti_score[2]-mbti_score[3] >0:
        answer += "F"
    elif mbti_score[2]-mbti_score[3] <0:
        answer += "C"
    else:
        answer += "C"

    if mbti_score[4]-mbti_score[5] >0:
        answer += "M"
    elif mbti_score[4]-mbti_score[5] <0:
        answer += "J"
    else:
        answer += "J"

    if mbti_score[6]-mbti_score[7] >0:
        answer += "N"
    elif mbti_score[6]-mbti_score[7] <0:
        answer += "A"
    else:
        answer += "A"

    print(mbti)
    print(mbti_score)

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"]	,[5, 3, 2, 7, 5]	))
print(solution(["TR", "RT", "TR"]	,[7, 1, 3]	))