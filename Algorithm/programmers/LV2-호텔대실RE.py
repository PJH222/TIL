def solution(book_time):
    answer = 0
    preprocess_time = []
    for i in book_time:
        stack = []
        for j in i:
            a = j.split(":")
            stack.append(int(a[0]) * 60 + int(a[1]))
        preprocess_time.append(stack)
    print(preprocess_time)

    rooms = [[]] * len(preprocess_time)

    for idx in range(len(rooms)):
        stack = []
        for i in preprocess_time:
            for j in preprocess_time:
                if i[1] + 10 <= j[0]:
                    if i not in stack and i not in rooms[idx]:
                        stack.append(i)
                        rooms[idx].append(i)
                    if j not in stack and j not in rooms[idx]:
                        stack.append(j)
                        rooms[idx].append(j)
        # rooms[idx].append(stack)
    print(rooms)




    return answer

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]	))
# print(solution([["09:10", "10:10"], ["10:20", "12:20"]]	))
# print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]	))
# print(solution([["09:10", "10:10"], ["10:20", "12:20"], ["09:00", "13:10"]]	))
# print(solution([["00:00", "10:10"], ["10:10", "10:11"],["10:00", "10:10"],["10:30", "10:40"]]))
#
# print(solution([["00:01", "00:10"], ["00:19", "00:29"]])) # 2
# print(solution([["08:00", "08:30"], ["08:00", "13:00"], ["12:30", "13:30"]]))# 2
# print(solution([["16:00", "16:10"], ["16:20", "16:30"], ["16:40", "16:50"]]))# 1
# print(solution([["09:10", "10:10"], ["10:20", "12:20"], ["12:30", "13:20"]])) # 1
# print(solution([["10:00", "10:10"]]))# 1