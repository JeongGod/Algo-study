def solution(routes):
    answer = 0
    routes.sort()
    cctv = -30001
    for start, end in routes:
        if start > cctv:
            answer += 1
            cctv = end
        else:
            if end < cctv:
                cctv = end
    return answer
