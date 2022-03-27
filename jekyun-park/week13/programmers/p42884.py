from collections import defaultdict
def solution(routes):
    
    answer = 1
    routes.sort(key=lambda x:x[0], reverse=True)
    
    current = routes[0][0]
    for route in routes[1:]:
        if route[1] >= current:
            continue
        else:
            current = route[0]
            answer += 1
    
    return answer