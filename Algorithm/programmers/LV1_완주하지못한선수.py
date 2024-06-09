# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    tmp1 = {} # 전체
    tmp2 = {} # 들어온 사람들
    
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
    
    for i in tmp1:
        if i not in tmp2:
            answer = i
            break
        
        else:
            tmp1[i] -= 1
                
    else:
        sorted_dictionary = sorted(tmp1.items(), key = lambda x:x[1], reverse=True)
        for i,j in sorted_dictionary:
            answer = i
            break
    #     print(sorted_dictionary)
    print(answer)
    
    return answer

solution(["leo", "kiki", "eden"]	,["eden", "kiki"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"],	["josipa", "filipa", "marina", "nikola"])
solution(["mislav", "stanko", "mislav", "ana"],	["stanko", "ana", "mislav"])
solution(["leo", "leo", "leo"]	,["leo", "leo"])
