# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    tmp1 = {} # 전체
    tmp2 = {} # 들어온 사람들
    
    # dictionary로 만들기
    for i in completion:
        if i not in tmp2:
            tmp2[i] = 1
        else:
            tmp2[i] += 1

    for i in participant:
        if i not in tmp1:
            tmp1[i] = 1
        else:
            tmp1[i] += 1
    
    # dictionary에 포함되는지 확인
    for i in tmp1:
        if i not in tmp2: # i가 없으면 answer에 할당하고 종료
            answer = i
            break
        
        elif i in tmp2 and tmp1[i] == tmp2[i]:
            continue
        
        else:
            answer = i
    print(answer)

    
    return answer

solution(["leo", "kiki", "eden"]	,["eden", "kiki"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"],	["josipa", "filipa", "marina", "nikola"])
solution(["mislav", "stanko", "mislav", "ana"],	["stanko", "ana", "mislav"])
solution(["leo", "leo", "leo"]	,["leo", "leo"])
solution(["leo", "leo", "leo", "leo", "leo","ana","ana","ana","ana"]	,["ana","leo", "leo", "leo", "leo","ana","ana","leo"])