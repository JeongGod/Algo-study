def solution(routes):
    answer = 0
    cam_pos = -30001
    routes.sort(key = lambda x : x[1])
    
    for route in routes:
     # 차량이 들어오는데 차량의 진입 위치가 현재 카메라의 위치보다 크다면 카메라를 추가적으로 설치하고 가장 최근 카메라의 위치는 현재 차량의 진출 지점이 된다.
        if(route[0] > cam_pos):
            answer += 1 # 카메라 설치
            cam_pos = route[1]
            
    return answer