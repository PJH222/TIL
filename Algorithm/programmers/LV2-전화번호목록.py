# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    diction = {}

    for i in phone_book:
        a = len(i)
        for j in range(1,a+1):
            if i[0:j] not in diction and j != a: # 접두사와 같은지 확인용
                diction[i[0:j]] = 0
            elif i[0:j] not in diction and j == a: #접두사로 사용 가능한 목록
                diction[i[0:j]] = 1
            elif i[0:j] in diction and diction[i[0:j]] == 1: #순차대로 찾을 때 찾은 경우
                return False
            elif i[0:a] in diction and diction[i[0:j]] == 0: # 이전의 결과를 다시 찾을 경우
                return False
    # print(diction)
    # print(solution(["119", "97674223", "1195524421"]))
    # print(solution(["123", "456", "789"]))
    # print(solution(["12", "123", "1235", "567", "88"]))

    # print(all_str)



    # 한 문장으로 정리해서 count하여 2이상이면 False 출력
    # all_str = ' '.join(phone_book)
    # print(all_str)
    # for i in phone_book:
    #     if all_str.count(i) > 1 and all_str.count(' ' + i) == 1:
    #         return False
    #     elif all_str.count(i) == 1:
    #         phone_book.remove(i)
    # print(phone_book)
    # print(all_str)



    # 완전탐색하여 False 출력
    # for i in phone_book:
    #     for j in phone_book:
    #         if i != j:
    #             if i in j or j in i:
    #                 return False
    #
    #         if j == phone_book[-1]:
    #             del phone_book[0]
    return answer


print(solution(["119", "97674223", "1195524421"]	))
print(solution(["123","456","789"]	))
print(solution(["12","123","1235","567","88"]))
print(solution([ "97674223", "1195524421","119"]	))

