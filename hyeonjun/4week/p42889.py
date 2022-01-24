def solution(N, stages):
    answer = {}
    # [스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수, 스테이지에 도달한 플레이어의 수, 스테이지 번호]
    failure_count = [[0, 0, (i+1)] for i in range(N)]
    stages.sort(reverse=True)

    for idx, stage in enumerate(stages):
        if stage > N:
            continue
        failure_count[stage-1][0] += 1
        failure_count[stage-1][1] = idx+1

    for stage in failure_count:
        if not stage[1]:  # avoid ZeroDivisionError
            answer[stage[2]] = 0
        else:
            answer[stage[2]] = stage[0]/stage[1]

    return sorted(answer, key=lambda x: answer[x], reverse=True)
