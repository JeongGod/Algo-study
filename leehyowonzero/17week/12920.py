import math

def solution(n, cores):

    if n <= len(cores):
        return n
    n -= len(cores)
    
    left = 1
    right = 10000 * n
    while left < right:
        mid = (left + right) // 2
        complete = 0
        for idx , core in enumerate(cores):
            complete += mid// core
        if complete >= n:
            right = mid
        else:
            left = mid + 1
    # mid 값이 만족되는 시간에 n개의 작업을 다 처리 할 수 있다. 그렇다면 마지막 작업은 누가 하였는가?
    complete = 0
    for idx , core in enumerate(cores):
        complete += right// core
    rest = complete - n
    candi = []
    for idx, core in enumerate(cores):
        if(right % core == 0):
            candi.append(idx+1)
    return candi[-1 - rest]