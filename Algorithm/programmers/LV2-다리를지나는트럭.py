# https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3
# 문제가 올라가고 난 이후에 지나간다 ~ 이런 의미 인건가??
def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = [] # 다리를 건너는 중인 트럭
    off_bridge = [] # 다리를 지난 트럭
    times = [] #트럭이 올라간 시각

    length = len(truck_weights)

    for time in range(1,bridge_length*len(truck_weights)+5):
        if len(times) > 0 and time == times[0] + bridge_length: #
            del times[0]
            off_bridge.append(on_bridge[0])
            del on_bridge[0]

        if time > 1 and len(on_bridge) == 0 and len(truck_weights) == 0 and len(off_bridge) == length:
            return time # 끝내기

        if len(on_bridge) == 0 and len(truck_weights) > 0: # 아예 비어있을 때 올리기
            on_bridge.append(truck_weights[0])
            del truck_weights[0]
            times.append(time)

        elif len(on_bridge) > 0 and len(truck_weights) > 0: # 차 한대가 있을 경우 하나더 올릴지말지 결정하고 올리기
            if sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights[0])
                del truck_weights[0]
                times.append(time) # 이후에 들어온놈들...




        # print(on_bridge,time)


    


    return answer


print(solution(2,10,[7,4,5,6]	))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]	))