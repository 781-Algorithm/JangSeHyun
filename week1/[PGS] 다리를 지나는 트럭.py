from collections import deque

def solution(bridge_length, weight, truck_weights):

    q = deque(truck_weights)
    running = deque()
    start_time = deque()
    
    answer = 0
    total_weight = 0
    
    while running or q:
        
        answer += 1
        
        if running:
            if start_time[-1] + bridge_length == answer:
                start_time.pop()
                total_weight -= running.pop()
                
        if q:
            if total_weight + q[0] <= weight:
                running.appendleft(q.popleft())
                start_time.appendleft(answer)
    
    return answer

print(solution(2,10,[7,4,5,6]))