import sys
from itertools import combinations


N, L, R, X = map(int, sys.stdin.readline().split())
difficulties = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(2, N + 1):
    for comb in combinations(difficulties, i):
        if L <= sum(comb) <= R:
            if max(comb) - min(comb) >= X:
                result += 1

print(result)
