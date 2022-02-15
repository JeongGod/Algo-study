def checkState(state):
    for el in state:
        x, y, a = el
        if a == 0: # 기둥
            if not (y == 0 or (x,y-1, 0) in state or (x,y,1) in state or (x-1,y,1) in state):
                return False
        else: # 보
            if not ((x, y-1, 0) in state or (x+1, y-1, 0) in state or ((x-1,y, 1) in state and (x+1, y, 1) in state)):
                return False
    return True

def solution(n, build_frame):
    answer = []
    now_state = set()
    for el in build_frame:
        x, y, a, b = el
        if b == 1: # 설치
            now_state.add((x, y, a))
        else: # 삭제
            now_state.remove((x, y, a))    
        if not(checkState(now_state)): # 설치 또는 삭제를 했는데 뭔가 문제가 있으면 행동 무르기
            if b == 1:
                now_state.remove((x, y, a))
            else:
                now_state.add((x, y, a))
            
    for el in now_state:
        answer.append(list(el))
    
    answer.sort()
    return answer