from collections import defaultdict
from typing import List


def create_schedule(start: int, end: int) -> None:
    if start == end:
        calendar[start] += 1
    else:
        for i in range(start, end+1):
            calendar[i] += 1


def get_consecutive_schedules() -> List[List[int]]:
    """
    연속된 일정들을 반환하는 함수
    """
    schdules = []
    dates = list(calendar.keys())
    start = 0

    for i in range(0, len(dates)):
        if i != len(dates)-1 and dates[i+1] - dates[i] == 1:
            continue

        else:
            schdules.append([dates[start], dates[i]])
            start = i+1

    return schdules


if __name__ == "__main__":
    global calendar
    calendar = defaultdict(int)
    answer: int = 0
    N = int(input())

    # 딕셔너리를 이용해 날짜별 일정의 개수를 파악
    for _ in range(N):
        start, end = map(int, input().split())
        create_schedule(start, end)

    calendar = dict(sorted(calendar.items()))
    schedules: List[List[int]] = get_consecutive_schedules()

    # 연속된 일정별로 일정의 개수가 가장 많은 날을 찾고 그 날의 일정 개수 기준으로 코팅지를 계산
    for schedule in schedules:
        start, end = schedule
        height = 0
        for i in range(start, end+1):
            if calendar[i] > height:
                height = calendar[i]
        answer += ((end - start + 1) * height)

    print(answer, end="\n")
