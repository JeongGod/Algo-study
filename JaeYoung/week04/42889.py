from typing import List


def solution(N, stages):
    stage_users: List[int] = [0] * N  # 스테이지별 유저수
    complete_users: int = 0  # 스테이지를 다 완료한 유저수
    stage_fail: List[(int, float)] = []  # 스테이지별 실패율

    for stage in stages:  # 스테이지별 유저수 구하기
        if stage == N+1:
            complete_users += 1
            continue
        stage_users[stage-1] += 1

    for idx, status in enumerate(stage_users):
        fail_rate: float = 0.0
        attend_users: int = status + complete_users

        for user in stage_users[idx + 1:]:
            attend_users += user

        if attend_users > 0:
            fail_rate = status / attend_users
        stage_fail.append((idx + 1, fail_rate))

    stage_fail.sort(key=lambda x: x[1], reverse=True)
    answer: List[int] = list(map(lambda x: x[0], stage_fail))

    return answer
