from collections import defaultdict
from typing import DefaultDict, List, Tuple
from datetime import datetime, timedelta


def init_shuttle_time(total_shuttle, interval) -> DefaultDict[str, List[str]]:
    """
    셔틀버스 시간표 생성 함수
    """
    shuttle_time: DefaultDict[str, List[str]] = defaultdict(list)
    start = datetime(year=2022, month=2, day=1, hour=9, minute=0)

    for i in range(total_shuttle):
        element = start + timedelta(minutes=i * interval)
        shuttle_time[element.strftime("%H:%M")]

    return shuttle_time


def people_all_same(time_list: List[str]) -> bool:
    """
    줄 선 사람들이 모두 같은 시간에 줄 섰는지 확인하는 함수
    """
    if len(set(time_list) & set(time_list)) == 1:
        return True
    else:
        return False


def calc_minute_diff(time: str, minute: int) -> str:
    return (
        datetime.strftime(
            datetime.strptime(time, "%H:%M")
            - timedelta(minutes=minute), "%H:%M")
    )


def solution(total_shuttle: int, interval: int, max_per_shuttle: int, time_table: List[str]):
    answer: str = ""
    time_table = sorted(time_table)
    shuttle_time: DefaultDict[str, List[str]] = init_shuttle_time(
        total_shuttle, interval)

    # 셔틀시간표 별로 대기하는 대기줄 생성
    for crew_time in time_table:
        for key in shuttle_time:
            if crew_time <= key and len(shuttle_time[key]) < max_per_shuttle:
                shuttle_time[key].append(crew_time)
                break

    shuttle_waits = sorted(shuttle_time.items(), reverse=True)

    for waits in shuttle_waits:
        time, people = waits

        # 제한 인원 보다 적은 대기 줄
        if len(people) < max_per_shuttle:
            answer = time
            break

        # 대기줄이 제한 인원과 같은 경우
        if len(people) == max_per_shuttle:
            if people_all_same(people):  # 모든 사람이 똑같은 시간에 와서 줄 선 경우
                answer = calc_minute_diff(people[0], 1)
                break
            else:  # 모든 사람이 똑같은 시간에 오진 않았음
                # 그런 경우에는 제일 늦게온 시각의 사람들 보다는 1분 빠르게 와야함
                tmp = sorted(list(set(people) & set(people)))
                last_people: str = tmp[-1]
                answer = calc_minute_diff(last_people, 1)
                break

    return answer
