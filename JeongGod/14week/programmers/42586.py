def solution(progresses, speeds):
    answer = []
    days = 0
    completes = 1
    for pro, speed in zip(progresses, speeds):
        nam = 100 - pro
        # 끝낼 수 있다면
        if days * speed >= nam:
            completes += 1
            continue
        # 끝낼 수 없다면
        else:
            answer.append(completes)
        nam -= (days * speed)
        x, y = divmod(nam, speed)
        # 정확히 나누어 떨어지지 않을 때
        if y != 0:
            x += 1
        days += x
        completes = 1
    answer.append(completes)
    return answer[1:]
