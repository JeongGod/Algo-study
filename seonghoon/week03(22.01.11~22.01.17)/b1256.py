import sys
from math import comb


input = sys.stdin.readline


def solve(a: int, z: int, target: int) -> str:
    if a == 0 or z == 0:
        return a * "a" + z * "z"

    startswitha: int = comb(a + z - 1, a - 1)
    if target <= startswitha:
        return "a" + solve(a - 1, z, target)
    return "z" + solve(a, z - 1, target - startswitha)


if __name__ == "__main__":
    n, m, k = map(int, input().split())

    if k <= comb(n + m, n):
        print(solve(n, m, k))
    else:
        print(-1)
