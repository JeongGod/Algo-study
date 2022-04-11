import heapq
a, b , n = map(int, input().split())
s_time = 0
j_time = 0
q = []
for _ in range(n):
    start_time, color, cnt = map(str,input().split())
    start_time = int(start_time)
    cnt = int(cnt)
    

    if color == 'B':  # 상민
        
        start_time = max(start_time, s_time)
        for i in range(cnt): 
            heapq.heappush(q, [start_time, 0])  # [time , color ] -> color 상민은 0
            start_time += a 
        s_time = start_time 

    elif color == 'R':  # 지수
        
        start_time = max(start_time, j_time)
        for i in range(cnt): 
            heapq.heappush(q, [start_time, 1])  # [time , color ] -> color 지수는 1
            start_time += b 
        j_time = start_time 

sangmin = []
jisu = []

for idx in range(1, len(q) + 1):
    time, color = heapq.heappop(q)
    if(color == 0):
        sangmin.append(idx)
    else:
        jisu.append(idx)
print(len(sangmin))
print(*sangmin)
print(len(jisu))
print(*jisu)
        
