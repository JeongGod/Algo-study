import copy
import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    max_val = max(arr)
    if max_val == 0:
        print(0)
        exit()
    visited = [[0, 0] for _ in range(max_val + 1)]  
    dq = deque([1])
    visited[1] = [0, 1]

    while dq:
        cur = dq.popleft()

        for idx, nval in enumerate([cur * 2, cur + 1]):
            if nval > max_val or visited[nval] != [0,0]:
                continue
            visited[nval] = copy.deepcopy(visited[cur])
            visited[nval][idx] += 1

            dq.append(nval)
    
    answer = 0
    max_mul = 0
    for val in arr:
        answer += visited[val][1]
        max_mul = max(max_mul, visited[val][0])
    answer += max_mul
    print(answer)
