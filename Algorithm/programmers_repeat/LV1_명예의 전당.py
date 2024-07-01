def solution(k, score):
    answer = []
    for i in range(len(score)):
        if i <= k - 1:
            bb = sorted(score[:i+1])
            answer.append(bb[0])
        else:
            bb = sorted(score[:i + 1])
            answer.append(bb[-k])
    return answer

solution(3,[10, 100, 20, 150, 1, 100, 200]	)
solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]	)