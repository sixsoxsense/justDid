jobs = [[0, 21], [1, 10], [2, 5], [3, 20], [4, 15], [5, 30], [6, 49], [7, 25], [8, 35], [9, 44], [10, 11]]
import heapq
from collections import deque

def jobs(jobs):
    return sorted(jobs)

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time

print(solution(jobs))