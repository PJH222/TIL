def turn_back(i,first, name,result):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum = 0
    first2 = first[:i] + first[i::-1] + first[:i:-1]
    name2 = name[:i] + name[i::-1] + name[:i:-1]
    print(name2)
    for j in range(len(first2)):
        # print(sum)

        if name2[j:].count("A") == len(name2[j:]): # 남은길이에 A만 남아있으면 멈추기
            result.append(sum)
            return

        if j < i: # 돌아가는 길에는 조이스틱 커서를 움직이는 숫자만 올리기
            sum += 1

        else: # "A" not in name2[j:]:
            sum += min(alpha.index(name2[j]), len(alpha) - alpha.index(name2[j])  )
            if j != 0 or j != len(name2) - 1 or name2[j+1:].count("A") == len(name2[j+1:]):
                sum += 1

        print((j,i),name2[j], (alpha.index(name2[j]), len(alpha) - alpha.index(name2[j])), sum)
    else: # 그냥 끝까지 다 돌았으면 마무리
        result.append(sum)
        return


def solution(name):
    # 다음 or 이전 알파벳인지는 안중요함
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    first = "A" * len(name)
    result = []
    sum = 0
    for i in range(len(name)):
        sum += min(alpha.index(name[i]), len(alpha) - alpha.index(name[i]))
        if i != len(name) - 1:
            sum += 1
        # print(sum,alpha.index(name[i]), len(alpha) - alpha.index(name[i]))
    result.append(sum)

    for i in range(len(name)):
        turn_back(i,first,name,result)
    print(result)

    return min(result) if min(result) != 0 else 0





# print(solution("JEROEN"	)) # 56
print(solution("JAN"	)) # 23
print(solution("JAZ"	)) # 11
# print(solution("A"	)) # 0
# print(solution("AA"	)) # 0
# print(solution("AAAAAAA"	)) # 0
# print(solution("AAAAAAZ"	)) # 2
# print(solution("ZAAAAAZ"	)) # 3
# print(solution("ZZAAAAZZZ"	)) # 10
# print(solution("ZZZZAAZZZ"	)) # 13
