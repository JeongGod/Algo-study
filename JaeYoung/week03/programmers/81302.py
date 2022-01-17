from typing import List


def isDistancing(place: List[str]) -> bool:
    x_direct: List[int] = [1, 0, -1, 0, 1, 1, -1, -1]
    y_direct: List[int] = [0, 1, 0, -1, 1, -1, -1, 1]
    person_position = []

    for i in range(len(place)):
        for j in range(len(place[i])):
            if place[i][j] == "P":
                person_position.append([i, j])

    for position in person_position:
        x, y = position

        for i in range(len(x_direct)):
            # 좌표이동
            new_x = x + x_direct[i]
            new_y = y + y_direct[i]

            # 이동좌표가 범위 밖
            if new_x < 0 or new_y < 0 or new_x > 4 or new_y > 4:
                continue

            if i < 4:  # 이동좌표 -> 상하좌우
                if place[new_x][new_y] == "P":  # 사람이 있는 경우 거리두기 X
                    return False

                # 이동한 칸이 O 이고 같은 방향으로 이동한 다음칸에 사람이 있는 경우 거리두기 X
                elif place[new_x][new_y] == "O":
                    nnew_x = new_x + x_direct[i]
                    nnew_y = new_y + y_direct[i]

                    if nnew_x < 0 or nnew_y < 0 or nnew_x > 4 or nnew_y > 4:
                        continue

                    if place[nnew_x][nnew_y] == "P":
                        return False

            else:  # 이동좌표 -> 대각선 방향 (↖ ↗ ↘ ↙)
                if place[new_x][new_y] == "P":
                    # 대각선 방향에 사람이 있고 인접한 칸이 O 이면 거리두기 X
                    if i == 4 and (place[x + 1][y] == "O" or place[x][y + 1] == "O"):
                        return False

                    if i == 5 and (place[x + 1][y] == "O" or place[x][y - 1] == "O"):
                        return False

                    if i == 6 and (place[x - 1][y] == "O" or place[x][y - 1] == "O"):
                        return False

                    if i == 7 and (place[x - 1][y] == "O" or place[x][y + 1] == "O"):
                        return False

    return True


def solution(places: List[List[str]]) -> List[int]:
    answer: List[int] = []

    for place in places:
        if isDistancing(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer