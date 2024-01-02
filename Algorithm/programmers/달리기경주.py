# https://school.programmers.co.kr/learn/courses/30/lessons/178871

# def solution(players, callings):
#     #앞뒤 순서 바꾸기
#     players_dic = {}
#     answer = []
#
#     # for i in callings:
#     #     # cnt = callings.count(i) #몇 번 불린 만큼 앞에 배치하면 됨 #`cnt로 해버리면 틀림`
#     #
#     #     idx = players.index(i) #현재 위치
#     #     players.insert(idx-1,i) # players에 불린 횟수만큼 앞의 자리에 삽입하기
#     #     del players[idx+1] #기존 위치는 삭제하기
#
# #실행횟수를 줄이는 방법...
#     #1~n까지 같은 원소만 출현했을 시에, 이를 한번에 위치 바꾸기
#     # a = len(callings)
#     # for i in range(a):
#     #     idx = players.index(callings[i])
#     #     front = players[idx-1]
#     #     players[idx-1] = players[idx]
#     #     players[idx] = front
#     #
#
#     a = len(players)
#     b = len(callings)
#     for i in range(a):
#         players_dic[i] = players[i]
#
#     for i in callings:
#         for key, val in players_dic.items() :
#             if val == i:
#                 abc = players_dic[key-1]
#                 players_dic[key-1] = i
#                 players_dic[key] = abc
#
#
#
#     return list(players_dic.values())


    # for i in range(len(callings)):




# print(solution(["mumu", "soe", "poe", "kai", "mine"]	,["kai", "kai", "mine", "mine"]	))
# ["mumu", "kai", "mine", "soe", "poe"]
# print(solution(["mumu", "soe", "poe", "kai", "mine"]	,["kai", "kai", "kai"]	))
# print(solution(["mumu", "soe", "poe", "kai", "mine"]	,["mine"]	))
# print(solution(["mumu", "soe", "poe", "kai", "mine"]	,["soe","mumu","soe","mumu"]	))

def solution(players, callings):

    players_ranking = {player: int(idx) for idx, player in enumerate(players)}

    # print(players_ranking)
    for call in callings: #call은 호명된 사람
        current_rank = players_ranking[call]
        players_ranking[call] -= 1                          #index로 찾는 것 보다 이렇게 하는게 훨씬 빠르니까..
        players_ranking[players[current_rank - 1]] += 1     #이 방식을 통해 index를 찾은 이후에, 변환하기
        players[current_rank - 1], players[current_rank] = call, players[current_rank - 1]  #결론적으로 보면 하나씩 바꾸는 것임...

    return players
print(solution(["mumu", "soe", "poe", "kai", "mine"]	,["kai", "kai", "mine", "mine"]	))
# ["mumu", "kai", "mine", "soe", "poe"]
print(solution(["mumu", "soe", "poe", "kai", "mine"]	,["kai", "kai", "kai"]	))
print(solution(["mumu", "soe", "poe", "kai", "mine"]	,["mine"]	))
print(solution(["mumu", "soe", "poe", "kai", "mine"]	,["soe","mumu","soe","mumu"]	))