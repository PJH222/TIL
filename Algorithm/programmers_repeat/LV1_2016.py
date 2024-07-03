def solution(a, b):
    answer = ''

    import datetime
    tmp = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer = tmp[datetime.date(2016,a,b).weekday()]


    return answer

solution(5,24)