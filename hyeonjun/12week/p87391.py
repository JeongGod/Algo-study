dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(n, m, x, y, queries):
    lx, rx, ly, ry = x, x+1, y, y+1
    for idx, dist in queries[::-1]:
        if idx == 0 and ly == 0:
            ry += dist
        elif idx == 1 and ry == m:
            ly -= dist
        elif idx == 2 and lx == 0:
            rx += dist
        elif idx == 3 and rx == n:
            lx -= dist
        else:
            lx += dx[idx]*dist
            ly += dy[idx]*dist
            rx += dx[idx]*dist
            ry += dy[idx]*dist

        if lx > n - 1 or rx < 0 or ly > m - 1 or ry < 0:
            return 0

        lx = max(0, lx)
        ly = max(0, ly)
        rx = min(n, rx)
        ry = min(m, ry)

    return (rx-lx)*(ry-ly)
