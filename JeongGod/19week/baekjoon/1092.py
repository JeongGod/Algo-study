import heapq
import sys

input = sys.stdin.readline

def solution(n, m, boxes, crains):
    answer = 0
    visited = set()
    while len(visited) < m:
        c_idx = 0
        b_idx = 0
        while b_idx < m and c_idx < n:
            # 가능하다면
            if not b_idx in visited and boxes[b_idx] <= crains[c_idx]:
                visited.add(b_idx)
                c_idx += 1
            b_idx += 1

        answer += 1
        if c_idx == 0:
            return -1
    return answer

if __name__ == "__main__":
    N = int(input())
    crains = sorted(list(map(int, input().split())), reverse=True)
    M = int(input())
    boxes = sorted(list(map(int, input().split())), reverse=True)

    print(solution(N, M, boxes, crains))

"""
3
6 8 9
5
9 9 9 7 8
"""
