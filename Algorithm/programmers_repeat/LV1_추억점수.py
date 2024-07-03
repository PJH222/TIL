def solution(name, yearning, photo):
    answer = []
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]

    for i in photo:
        tmp = 0
        for j in i:
            if j in dict:
                tmp += dict[j]
        else:
            answer.append(tmp)
    print(answer)


    return answer

solution(["may", "kein", "kain", "radi"]	,[5, 10, 1, 3]	,[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]	)
solution(["kali", "mari", "don"]	,[11, 1, 55]	,[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]	)

