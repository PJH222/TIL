# 똑같이 틀리는데 뭐가 잘못된거지...

def turn_back(i,name,result):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    sum = 0
    if i != -1:
        name2 = name[:i] + name[i::-1] + name[:i:-1]
    else:
        name2 = name
    
    sum = 0 # 이동 횟수에 대한 움직임 횟수를 미리 더 해놓기
    # print(name2, sum)

    for j in range(len(name2)):
        # A만 남은 경우 끝내기
        if name2[j:].count("A") == len(name2[j:]): 
            result.append(sum - len(name2[j:]) - 1) # 덜 움직인 거리만큼 다시 빼주기
            # print("중간에 끝난 경우)")
            # print(i,"sum :",(sum - len(name2[j:]) - 1))
            # print("빼주는 숫자 :", len(name2[j:]) - 1 )
            return

        # back 하기 전에는 그냥 지나가지
        if j < i:
            continue
        elif name2[j] == "Z":
            sum += 1
        # A가 아닌 경우,
        elif name2[j] != "A":
            sum += min(alpha.index(name2[j]), len(alpha) - 1 - alpha.index(name2[j]) + 1)
            sum += 1
            # print("i :", i, "j :", j,"alpha :",name2[j], "min :",alpha.index(name2[j]), len(alpha) - 1 - alpha.index(name2[j]) + 1)

        elif name2[j] == "A":
            continue

    else: # 최종까지 순회한 경우
        result.append(sum)
        # print(i,sum)
        # print("끝까지 간 경우)","i :", i, "j :", j, "sum :",sum)
        return


def solution(name):
    # 다음 or 이전 알파벳인지는 안중요함
    result = []
    for i in range(-1,len(name)-1):
        turn_back(i,name,result)

    # print(result)

    answer = min(result)
    return answer if answer > 0 else 0





print(solution("JEROEN"	)) # 56
print(solution("JAN"	)) # 23
print(solution("JAZ"	)) # 11
print(solution("A"	)) # 0
print(solution("AA"	)) # 0
print(solution("AAAAAAA"	)) # 0
print(solution("AAAAAAZ"	)) # 2
print(solution("ZAAAAAZ"	)) # 3
print(solution("ZZAAAAZZZ"	)) # 10
print(solution("ZZZZAAZZZ"	)) # 14 <<< 이거만 계속 틀리는데...?
print(solution("ABCD"))