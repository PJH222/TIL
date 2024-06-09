# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    results = [0,0,0]
    
    aa = [1,2,3,4,5] * (10000 // 5)
    bb = [2,1,2,3,2,4,2,5] * (10000 // 8)
    cc = [3,3,1,1,2,2,4,4,5,5] * (10000 // 10)
    
    for i in range(len(answers)):
        if answers[i] == aa[i]:
            results[0] += 1
    
        if answers[i] == bb[i]:
            results[1] += 1
        
        if answers[i] == cc[i]:
            results[2] += 1
    
    maxx = max(results)
    
    if results.count(maxx) > 1:
        for i in range(len(results)):
            if results[i] == maxx:
                answer.append(i + 1)

        answer = sorted(answer)
        
    else:
        for i in range(len(results)):
            if results[i] == maxx:
                answer.append(i + 1)

    return answer

# solution(11)
solution([1,2,3,4,5])
solution([1,3,2,4,2]	)
