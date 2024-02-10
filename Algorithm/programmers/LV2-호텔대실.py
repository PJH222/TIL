def solution(book_time):
    answer = 0
    preprocess_time = []
    time_range = []

    for i in book_time:
        stack = []
        for j in i:
            a = j.split(":")
            b = int(a[0]) * 60 + int(a[1])
            stack.append(b)
        time_range.append(range(stack[0],stack[1] + 1)) # 범위
        preprocess_time.append(stack) # 숫자로만 표현한 리스트

    room = [[]] * len(book_time) # 최대 방 개수만큼 우선 방 만들기
    used = [] # 이미 배정이 시간대
    
    for i in range(len(preprocess_time)):
        stack = []
        minn = 2000
        for j in range(len(preprocess_time)):
            if preprocess_time[i][1] + 10 <= preprocess_time[j][0] and preprocess_time[j][0] - preprocess_time[i][0] < minn:
                minn = preprocess_time[j][0] - preprocess_time[i][0]
                if preprocess_time[i] not in used:
                    stack.append(preprocess_time[i])
                if preprocess_time[j] not in used:
                    stack.append(preprocess_time[j])
                used.append(preprocess_time[i])
                used.append(preprocess_time[j])
        else:
            room[i] = stack
        # print(room)
        # if len(room[i]) == 0:
        #     room[i].append(preprocess_time[i])
    # print(used)
    # print(preprocess_time)
    for i in used:
        if i in preprocess_time:
            preprocess_time.remove(i)

    cnt = 0
    for i in range(len(room)):
        if len(room[i]) == 0 and len(preprocess_time) > 0:
            a = preprocess_time.pop()
            room[i] = [a]

        if len(room[i]) == 0:
           cnt += 1

    for i in range(cnt):
        room.pop()

    answer = len(room)
    print(room)
    # print(preprocess_time)

    return answer

#
# print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]	))
# print(solution([["09:10", "10:10"], ["10:20", "12:20"]]	))
# print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]	))
# print(solution([["09:10", "10:10"], ["10:20", "12:20"], ["09:00", "13:10"]]	))
# print(solution([["00:00", "10:10"], ["10:10", "10:11"],["10:00", "10:10"],["10:30", "10:40"]]))

# print(solution([["00:01", "00:10"], ["00:19", "00:29"]])) # 2

# print(solution([["08:00", "08:30"], ["08:00", "13:00"], ["12:30", "13:30"]]))# 2

print(solution([["16:00", "16:10"], ["16:20", "16:30"], ["16:40", "16:50"]]))# 1

print(solution([["09:10", "10:10"], ["10:20", "12:20"], ["12:30", "13:20"]])) # 1

# print(solution([["10:00", "10:10"]]))# 1