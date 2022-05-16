import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    limits = list(map(int, input().split()))
    M = int(input())
    weights = list(map(int, input().split()))

    limits.sort(reverse=True)
    weights.sort(reverse=True)

    if weights[0] > limits[0]:
        print(-1)

    else:
        time = 0
        while weights:
            for crane in limits:
                for box in weights:
                    if crane >= box:
                        weights.remove(box)
                        break
            time += 1
        print(time)
