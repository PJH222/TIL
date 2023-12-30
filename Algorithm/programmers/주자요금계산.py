import math
def solution(fees, records):
    times = [] #입출고 차량의 시간 기록을 분단위로 환산한 리스트
    num = [] #입출고 차량 번호의 기록 리스트
    result = [] #중복을 제외한 오름차 순 차량 번호의 기록 리스트
    inou = []

    #도든 시간을 분단위로 환산
    for i in records:
        a = i.split()[0]
        b = a.split(":")
        c = int(b[0]) * 60 + int(b[1])
        times.append(c)
        num.append(i.split()[1])
        inou.append(i.split()[2])

    #중복없이 오름차순으로 차량 번호판 정리
    for i in num:
        if i not in result:
            result.append(i)
    result.sort()

    answer = [0 for x in range(len(result))]
    answers = [0 for x in range(len(result))]
    for i in result:
        if num.count(i) % 2:
            num.append(i)
            times.append(23*60 + 59)
            inou.append("OUT")

    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] == num[j] and inou[i] == "IN" and inou[j] == "OUT":
                diff = times[j]-times[i]
                idx = result.index(num[i])
                answer[idx] += diff
                break

    #print(answer)

    for i in range(len(answer)):
        if answer[i] > fees[0]:
            answers[i] = fees[1] + math.ceil((answer[i]-fees[0])/fees[2])*fees[3]
        else:
            answers[i] = fees[1]
    print(answers)

    return answers

solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"] )
# [14600, 34400, 5000]

solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
# [0, 591]

solution([1, 461, 1, 10],["00:00 1234 IN"])
# [14841]
