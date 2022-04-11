import heapq

n = int(input())
arr = [None for _ in range(n)]
for i in range(n):
    fm, to = map(int,input().split())
    if(fm <= to):
        arr[i] = [fm, to]
    else:
        arr[i] = [to, fm]
d = int(input())

arr.sort(key= lambda x: (x[1], x[0]))
q = []
answer = 0
for fm, to in arr:
    if not q:
        if not (to - fm <= d):
            continue
        heapq.heappush(q, [fm, to])
        end = fm
        start = end - d
    else:
        if not (to - fm <= d):
            continue
        if(to <= end):
            heapq.heappush(q, [fm, to])
        else:
            
            while (q and q[0][0]+d < to):
                heapq.heappop(q) 
            heapq.heappush(q, [fm, to])
            end = q[0][1]
            start = end - d
    answer = max(answer, len(q))
print(answer)