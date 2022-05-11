import sys
from itertools import product

input = sys.stdin.readline

if __name__ == "__main__":
    target = input().rstrip()

    broken = int(input())
    buttons = []
    if broken != 0:
        buttons = list(map(int, input().split()))

    answer = abs(100 - int(target))
    possibles = [i for i in range(10) if i not in buttons]
    for cnt in range(len(target) - 1, len(target) + 2):
        if cnt == 0 or cnt == 7:
            continue
        for pro in product(possibles, repeat=cnt):
            val = int("".join(list(map(str, pro))))
            answer = min(answer, abs(val - int(target)) + cnt)
    print(answer)
