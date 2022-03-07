import sys
input = sys.stdin.readline


def dp():
    arr = [[0 for _ in range(3)] for _ in range(n+1)]
    for idx, point in enumerate(stair):
        arr[idx+1][0] = max(arr[idx][1], arr[idx][2])
        arr[idx+1][1] = arr[idx][0]+point
        arr[idx+1][2] = arr[idx][1]+point
    return max(arr[-1][1:])


if __name__ == "__main__":
    n = int(input())
    stair = [int(input()) for _ in range(n)]
    print(dp())
