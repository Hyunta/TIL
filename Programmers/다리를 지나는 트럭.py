from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    cnt = 0
    b_weight = 0
    
    while bridge:
        cnt += 1
        b_weight -= bridge.popleft()
        if truck_weights:
            if b_weight+truck_weights[0] <= weight:
                b_weight += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return cnt

'''

큐를 이용해서 브릿지를 구현하려고함
브릿지의 길이 만큼 0을 넣어서 컨베이어벨트처럼 돌리고
마지막차가 지나갈 때 모든 0을 삭제하며 종료되는 while 문

효율적인 문제점
sum(bridge) 를 계속 반복하다 보니 시간복잡도가 커졌고
sum을 활용하지 않고 트럭이 다리위로 올라올 때 추가해주고
다리에서 내려갈 때 빼주는 형식을 통해 개선

'''