import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
ts = {0: 1, 1: 2, 2: 3, 3: 0}


def dot(curve):
    dots = set()
    for x, y, w, g in curve:
        nx = x + dx[w]
        ny = y + dy[w]
        dots.add((x, y))
        dots.add((nx, ny))
        direction = [w]
        for _ in range(g):
            for i in direction[::-1]:
                direction.append(ts[i])
                dots.add((nx+dx[ts[i]], ny+dy[ts[i]]))
                nx += dx[ts[i]]
                ny += dy[ts[i]]
    return dots


def check_square(dots):
    ans = 0
    for x, y in dots:
        if (x+1, y) in dots and (x, y+1) in dots and (x+1, y+1) in dots:
            ans += 1
    return ans


if __name__ == "__main__":
    answer = 0
    n = int(input())
    curve = [list(map(int, input().split())) for _ in range(n)]
    dots = dot(curve)
    print(check_square(dots))
