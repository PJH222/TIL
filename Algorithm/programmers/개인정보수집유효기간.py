# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    answer = []
    today_list = today.split(".") #오늘 날짜를 일수로만 계산하기
    today_days = int(today_list[2]) + int(today_list[1]) * 29 + int(today_list[0]) * 29 * 12
    len_terms = len(terms)
    pri = privacies # 축약어
    
    for i in pri:
        pri_list = i.split()
        start_days = pri_list[0].split(".")
        indict = pri_list[1]
        for j in range(len(terms)):
            if indict in terms[j]: # 유효기간을 일수로만 계산하기
                deadline_in_days = int(start_days[2]) + int(start_days[1]) * 29 + int(start_days[0]) * 29 * 12 + int(terms[j].split(" ")[1])*29
                if deadline_in_days <= today_days: # 유효기간이 오늘 날짜보다 작은 경우에 append하기
                    answer.append(pri.index(i)+1)
                print(deadline_in_days, today_days)

    return answer
print(solution("2022.05.19"	,["A 6", "B 12", "C 3"]	,["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	))
