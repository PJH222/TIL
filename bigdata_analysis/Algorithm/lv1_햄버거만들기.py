def solution(ingredient):
    answer = 0
    i = 0
    b = len(ingredient)
    
    while i < b - 3:
        # print(ingredient[i:i+4], ingredient)
        if ingredient[i:i+4] == [1,2,3,1]:
            answer += 1
            del ingredient[i:i+4]
            b = len(ingredient)
            # print(ingredient[i:i+4],i,ingredient)
            # del ingredient[i:i+4]
            if i > 4:
                i -= 3
            else:
                i = 0
            
        else:
            i += 1
            
    # print()
    # print(ingredient, i, answer)
    return answer



solution([2, 1, 1, 2, 3, 1, 2, 3, 1]	) # 2
solution([1, 3, 2, 1, 2, 1, 3, 1, 2]	) # 0
solution([1,2,3,1,1,2,3,1])