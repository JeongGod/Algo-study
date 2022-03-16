from collections import deque
import sys
input = sys.stdin.readline


def count(pizza, piece):
    res = [0 for _ in range((sum(pizza) + 1))]
    res[0] = 1
    res[-1] = 1
    for i in range(piece):
        summation = 0
        queue = deque(pizza)
        for _ in range(i):
            queue.rotate(-1)
        queue.pop()
        while queue:
            summation += queue.popleft()
            res[summation] += 1
    return res


if __name__ == "__main__":
    answer = 0

    target = int(input())
    m, n = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    b = [int(input()) for _ in range(n)]
    a_count = count(a, m)
    b_count = count(b, n)

    for i in range(target + 1):
        if 0 <= i < len(a_count) and 0 <= target-i < len(b_count):
            answer += a_count[i] * b_count[target-i]
    print(answer)
