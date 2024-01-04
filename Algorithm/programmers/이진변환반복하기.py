# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    x , y = 0 , 0
    #x,y라하면, x = 이진변환 횟수 ,y = 총 0 제거 수
    cnt = s.count("1")
    cnt_y = s.count("0")
    result = format(cnt, 'b')
    x += 1
    y += cnt_y

    while result != "1":
        cnt = result.count("1")
        cnt_y = result.count("0")
        x += 1
        y += cnt_y

        result = format(cnt, 'b')
        print(result)

    answer = [x, y]
    return answer

print(solution("110010101001"	))
print(solution("01110"	))
print(solution("1111111"	))

