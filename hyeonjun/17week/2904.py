import sys
from collections import Counter
input = sys.stdin.readline


def factorization(x):
    d = 2
    dup = 0
    set_prime, arr_prime = set(), []
    while d <= x:
        if not x % d:
            x /= d
            set_prime.add((d, dup))
            arr_prime.append(d)
            dup += 1
        else:
            d += 1
            dup = 0
    return set_prime, arr_prime


if __name__ == "__main__":
    N = int(input())
    paper = list(map(int, input().split()))
    prime = []
    cand = set()
    answer = [1, 0]

    for i, num in enumerate(paper):
        set_prime, arr_prime = factorization(num)
        paper[i] = set_prime
        prime += arr_prime

    for num, frequency in Counter(prime).items():
        dup = 0
        while frequency >= N:
            answer[0] *= num
            cand.add((num, dup))
            dup += 1
            frequency -= N

    for i in paper:
        answer[1] += len(cand - i)
    print(*answer)
