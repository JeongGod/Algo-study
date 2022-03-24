def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    
    out_t = routes[0][1]
    for r in routes:
        if r[0] > out_t:
            # 지금 저장해둔 out_t에 대한 카메라 설치
            answer += 1
            out_t = r[1]
    # 마지막 차에 대한 카메라
    answer += 1
    return answer
