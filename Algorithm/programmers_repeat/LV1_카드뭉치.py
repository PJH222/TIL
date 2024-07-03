def solution(cards1, cards2, goal):
    answer = ''
    for i in range(len(goal)):
        if len(cards1) > 0 and cards1[0] == goal[i]:
            del cards1[0]
            continue

        if len(cards2) > 0 and cards2[0] == goal[i]:
            del cards2[0]
            continue

        if 1:
            return "No"
    print(cards1, cards2)

    return "Yes"

solution(["i", "drink", "water"]	,["want", "to"]	, ["i", "want", "to", "drink", "water"]	)
solution(["i", "water", "drink"]	,["want", "to"]	,["i", "want", "to", "drink", "water"]	)