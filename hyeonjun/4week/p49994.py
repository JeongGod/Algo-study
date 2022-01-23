MOVE = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def solution(dirs):
    location = set()
    x, y = 0, 0
    for dir in dirs:
        dx, dy = MOVE[dir]
        nx = x + dx
        ny = y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            location.add((x, y, nx, ny))
            location.add((nx, ny, x, y))
            x, y = nx, ny

    return len(location)//2
