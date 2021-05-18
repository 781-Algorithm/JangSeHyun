# 왜 테스트 케이스 하나가 통과가 안될까...
from collections import deque
import heapq

def solution(jobs):
    length = len(jobs)
    time = 0

    jobs.sort()
    jobs = deque(jobs)
    
    q = []
    req, dur = jobs.popleft()  # [요청시간, 소요시간]
    heapq.heappush(q, [dur, req])  # heap은 [소요시간, 요청시간] 순으로 들어간다
    now = req

    while q:
        dur, req = heapq.heappop(q)

        if now >= req:
            time += now - req + dur
            now += dur

        else:
            time += dur
            now = req + dur

        flag = False

        while jobs and jobs[0][0] < now:
            r, d = jobs.popleft()
            heapq.heappush(q, [d, r])
            flag = True

        if jobs and not flag:  # 동떨어진 req가 존재할 때
            r, d = jobs.popleft()
            heapq.heappush(q, [d, r])

    return time // length