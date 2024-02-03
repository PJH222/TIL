def solution(cap, n, deliveries, pickups):
    answer = 0

    delivery(cap, n, deliveries, answer)
    pickup(cap, n, pickups, answer)

    return answer


def delivery(cap, n, deliveries, answer):
    print(deliveries)
    if len(deliveries) == 0:
        return

    if deliveries[-1] != 0:
        gap = deliveries[-1] - cap

        if gap < 0:
            for i in range(len(deliveries)):
                a = deliveries[i:]
                if sum(a) > cap :
                    for _ in range(i):
                        deliveries.pop()
                    deliveries[-1] -= sum(a) - cap
                    break

        elif gap == 0:
            deliveries.pop()
            # answer += len(deliveries) - 1
        else:
            deliveries[-1] = gap
            answer += len(deliveries) - 1

        if len(deliveries) == 0:
            return answer

    else:
        deliveries.pop()

    return delivery(cap, n, deliveries, answer)


def pickup(cap, n, pickups, answer):
    if len(pickups) == 0:
        return

    if pickups[-1] != 0:
        gap = pickups[-1] - cap

        if gap <= 0:
            pickups.pop()
            pickups[-1] += gap
            answer += len(pickups) - 1  # 인덱스
        else:
            pickups[-1] = gap
            answer += len(pickups) - 1

        if len(pickups) == 0:
            return answer
    else:
        pickups.pop()

    return pickup(cap, n, pickups, answer)


print(solution(4,5,[1, 0, 3, 1, 2]	,[0, 3, 0, 4, 0]	))
