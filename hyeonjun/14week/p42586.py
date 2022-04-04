from math import ceil


def solution(progresses, speeds):
    answer = []
    prior = 0

    for progress, speed in zip(progresses, speeds):
        need_time = ceil((100-progress)/speed)
        if prior < need_time:
            answer.append(1)
            prior = need_time
        else:
            answer[-1] += 1

    return answer
