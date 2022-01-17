dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def check(place):
    for x in range(5):
        for y in range(5):
            if place[x][y] == "P":
                for i in range(3):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if place[nx][ny] == "X":
                            continue
                        elif place[nx][ny] == "P":
                            return 0
                        else:
                            cnt = 0
                            for j in range(4):
                                nnx = nx + dx[j]
                                nny = ny + dy[j]
                                if (
                                    0 <= nnx < 5
                                    and 0 <= nny < 5
                                    and place[nnx][nny] == "P"
                                ):
                                    cnt += 1
                                    if cnt > 1:
                                        return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer
