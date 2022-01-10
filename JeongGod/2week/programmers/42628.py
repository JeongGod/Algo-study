import heapq
def solution(operations):
    """
    길이로 비교하자.
    """
    max_hq, min_hq = [], []
    cnt = 0
    for oper in operations:
        com, num = oper.split()
        num = int(num)
        
        if com == "I":
            cnt += 1
            heapq.heappush(max_hq, -num)
            heapq.heappush(min_hq, num)
        elif com == "D":
            cnt -= 1
            # 다 뺏다면
            if cnt <= 0:
                cnt = 0
                max_hq, min_hq = [], []
                continue
                
            if num == 1:
                heapq.heappop(max_hq)
            else:
                heapq.heappop(min_hq)
    
    return [-max_hq[0], min_hq[0]] if cnt > 0 else [0, 0]