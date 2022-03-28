import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    black = set()
    for _ in range(n):
        x, y = map(int, input().split())
        for i in range(x, x+10):
            for j in range(y, y+10):
                black.add((i, j))

    print(len(black))
