import sys
from math import factorial

input = sys.stdin.readline


def permutation_count(a, b):
    return factorial(a+b) // (factorial(a) * factorial(b))


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    if K > permutation_count(N, M):
        print(-1)

    else:
        ans = ""
        K -= 1
        while N != 0 and M != 0:
            count = permutation_count(N-1, M)

            if K < count:
                ans += "a"
                N -= 1

            else:
                ans += "z"
                M -= 1
                K -= count

        ans += "z" * M + "a" * N

        print(ans)
