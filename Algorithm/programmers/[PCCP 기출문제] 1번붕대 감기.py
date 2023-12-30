# https://school.programmers.co.kr/learn/courses/30/lessons/250137

def solution(bandage, health, attacks):
    heal = health #현재 체력
    now_time = attacks[0][0] #시각
    end_time = attacks[-1][0] #마지막 공격 시각
    idx = 0 #공격 타이밍
    healing = 0 #힐링 누적시간

    for i in range(attacks[0][0],end_time+1):
        if now_time == attacks[idx][0]:
            healing = 0
            heal -= attacks[idx][1]
            if heal <= 0:
                return -1
            else:
                idx += 1
        else:
            heal += bandage[1]
            healing += 1
            if healing == bandage[0]:
                heal += bandage[2]
                healing = 0
            if heal >= health:
                heal = health
        # print(heal,idx)

        now_time += 1


    return heal

print(solution([5, 1, 5]	,30,[[2, 10], [9, 15], [10, 5], [11, 5]]	))
print(solution([3, 2, 7]	,20,[[1, 15], [5, 16], [8, 6]]	))
print(solution([4, 2, 7]	,20,[[1, 15], [5, 16], [8, 6]]	))
print(solution([1, 1, 1]	,5,[[1, 2], [3, 2]]	))