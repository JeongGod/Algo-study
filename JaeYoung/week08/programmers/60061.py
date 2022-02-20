# 기둥 조건 (0)
# 1. 바닥 위에 있다.
# 2. 보의 한쪽 끝 부분 위에 있다.
# 3. 또 다른 기둥 위에 있다.

# 보 조건 (1)
# 1. '한쪽' 끝 부분이 기둥 위에 있다.
# 2. 양쪽 끝 부분이 다른 보와 동시에 연결되어 있다.

# 삭제 -> 0 , 설치 -> 1
# 구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제
# 바닥에 보를 설치 하는 경우는 없습니다.
# 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.

# 아이디어
# build_frame 을 삭제, 설치할 때 조건들에 적합한지 검사하고 수행

def is_possible(check) -> bool:
    for x, y, building in check:

        if building == 0:  # 기둥
            if y == 0 or [x-1, y, 1] in check or [x, y, 1] in check or [x, y-1, 0] in check:
                continue
            else:
                return False
        else:  # 보
            if ([x, y-1, 0] in check or [x+1, y-1, 0] in check or
                    ([x-1, y, 1] in check and [x+1, y, 1] in check)):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    check_list = []

    for item in build_frame:

        x, y, building, task = item

        if task == 1:  # 설치
            check_list.append([x, y, building])
            if not is_possible(check_list):
                check_list.remove([x, y, building])
        else:  # 삭제
            check_list.remove([x, y, building])
            if not is_possible(check_list):
                check_list.append([x, y, building])

    return [[]] if len(check_list) == 0 else sorted(check_list)


# print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
#       1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
