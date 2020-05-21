'''
time>=인 리스트 정렬
    time+(jobs[1]-jobs[0])
'''

jobs = [[0, 3], [1, 5],[2,3],[3,1]]

from heapq import heappop, heappush


def solution(jobs):
    count = 0
    end = 0
    start = -1
    wait = []
    answer = 0
    while count < len(jobs):
        for job in jobs:
            if start < job[0] <= end:
                answer += end - job[0]
                heappush(wait, job[1])
        if wait:
            answer += wait[0] * len(wait)
            start = end
            end += heappop(wait)
            count += 1
        else:
            end += 1
    return answer // len(jobs)
'''
이 문제는 SJF알고리즘을 말하는것으로
최소평균을 구하기위해선 최소 실행시간을 우선적으로 작동하면 되는것이다.
요청된 job이 실행되는 시간 즉 job[1]동안 요청이 들어온 작업에 대해 
job[1]에 대한 최소힙을 적용하여 최소 실행시간인 작업을 우선적으로 한다.
level3 답게 생각할 조건이 많아 힘들었고 
코딩중 값처리에 대해 의문이 계속 생겨 다른사람의 코드 
'''

print("솔루션", solution(jobs))
