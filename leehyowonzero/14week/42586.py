import math

def solution(progresses, speeds):
    answer = []
    distribution_date = [None for _ in range(len(progresses))]
    for idx, progress in enumerate(progresses):
        rest = 100 - progress
        days  = math.ceil(rest / speeds[idx])
        if(idx != 0):
            if(distribution_date[idx-1] > days):
                distribution_date[idx] = distribution_date[idx-1]
            else:    
                distribution_date[idx] = days
            continue
        distribution_date[idx] = days
        
    now_date = None
    idx = -1
    for el in distribution_date:
        if(now_date == el):
            answer[idx] += 1
        else:
            answer.append(1)
            now_date = el
            idx += 1
    return answer