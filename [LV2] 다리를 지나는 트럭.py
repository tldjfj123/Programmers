from collections import deque

n, w, l = map(int , input().split())
t = list(map(int, input().split()))

def solution(bridge_length, weight, truck_weights):
    n = len(truck_weights)
    truck_weights = deque(truck_weights)
    arrived = []
    stack = deque([])
    answer = 0
    time = deque([])
    
    while len(arrived) != n :
        if len(time) > 0 :
            for i in range(len(time)) :
                time[i] += 1
                
        answer += 1
        
        if len(stack) == 0 :
            stack.append(truck_weights.popleft())
            time.append(0)
        else :
            if time[0] == bridge_length :
                time.popleft()
                arrived.append(stack.popleft())
                if len(truck_weights) >= 1 :
                    if truck_weights[0] + sum(stack) <= weight :
                        stack.append(truck_weights.popleft())
                        time.append(0)
            else :
                if len(truck_weights) >= 1 :
                    if truck_weights[0] + sum(stack) <= weight :
                        stack.append(truck_weights.popleft())
                        time.append(0)
                    else :
                        continue
                else :
                    continue
        
    return answer

print(solution(w, l, t))