import heapq

def solution(food_times, k):
    q = []
    for i, el in enumerate(food_times):
        heapq.heappush(q, [el, i+1])
        
    before_eating = 0
    restfood = len(food_times)
    while q :
        if(k >= restfood * (q[0][0] - before_eating)):
            k -= restfood * (q[0][0] - before_eating)
            restfood -= 1
            before_eating = q[0][0]
            heapq.heappop(q)  
        else:
            break
    if not (q):
        return -1
    k = k % restfood
    q.sort(key = lambda x : x[1])
    answer = q[k][1]
    return answer