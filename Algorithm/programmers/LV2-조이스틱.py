def turn_back(i,first, name,result):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum = 0
    first2 = first[:i] + first[i::-1] + first[:i:-1]
    name2 = name[:i] + name[i::-1] + name[:i:-1]
    # print(name2)
    for j in range(len(first2)):
        # print(alpha.index(name2[j]), len(alpha) - alpha.index(name2[j]),sum)
        if name2[j:].count("A") == len(name2[j:]): # 남은길이에 A만 남아있으면 멈추기
            result.append(sum)
            break

        if j < i:
            sum += 1
        elif "A" not in name2[j:]:
            sum += min(alpha.index(name2[j]), len(alpha) - alpha.index(name2[j])  )
            sum += 1
        else:
            sum += min(alpha.index(name2[j]), len(alpha) - alpha.index(name2[j]) )
            sum += 1



        # elif "A" in name2[j:]: # A가 있긴한데, 어중간하게 남은 경우

    else:
        result.append(sum)
        return

def solution(name):
    # 다음 or 이전 알파벳인지는 안중요함
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    first = "A" * len(name)
    result = []
    sum = 0
    for i in name:
        sum += min(alpha.index(i), len(alpha) - alpha.index(i))
        sum += 1
        # print(alpha.index(i), len(alpha) - alpha.index(i))
    result.append(sum)

    for i in range(len(name)):
        turn_back(i,first,name,result)
    print(result)

    return min(result) - 1 if min(result) != 0 else 0





print(solution("JEROEN"	)) # 56
print(solution("JAN"	)) # 23
print(solution("JAZ"	)) # 11
print(solution("A"	)) # 0
print(solution("AA"	)) # 0
print(solution("AAAAAAA"	)) # 0
print(solution("AAAAAAZ"	)) # 2
print(solution("ZAAAAAZ"	)) # 3
print(solution("ZZAAAAZZZ"	)) # 10
print(solution("ZZZZAAZZZ"	)) # 13
