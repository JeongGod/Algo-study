import sys
from math import ceil
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    infos = []
    sum_population = 0
    for _ in range(N):
        village, population = map(int, input().split())
        infos.append([village, population])
        sum_population += population

    infos.sort()
    sum_population = ceil(sum_population/2)

    count = 0
    for village, population in infos:
        count += population
        if count >= sum_population:
            print(village)
            break
