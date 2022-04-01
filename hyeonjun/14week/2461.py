from heapq import heappush, heappop
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    answer = float('inf')
    N, M = map(int, input().split())
    classes = [list(map(int, input().split())) for _ in range(N)]

    cand = []
    maxVal = 0
    for idx, classe in enumerate(classes):
        classe.sort()
        heappush(cand, (classe[0], idx, 0))
        maxVal = max(maxVal, classe[0])

    answer = maxVal - cand[0][0]
    while cand:
        status, classe, idx = heappop(cand)
        if idx == M - 1:
            break
        heappush(cand, (classes[classe][idx+1], classe, idx+1))
        maxVal = max(maxVal, classes[classe][idx+1])
        answer = min(answer, maxVal - cand[0][0])

    print(answer)
