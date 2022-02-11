from typing import List


def hour_to_min(s : str) -> int:
    hour, minute = map(int, s.split(":"))
    return 60*hour + minute

def min_to_hour(t : int) -> str:
    return f"{t // 60:02}:{t % 60:02}"


def find_last_person(n : int, m : int, t : int, mtimetable : List[int]) -> int:
    cur = hour_to_min("09:00")
    person_idx = 0
    # 셔틀버스 이전에 사람들을 센다.
    for _ in range(n):
        shuttle_cnt = 0
        while shuttle_cnt < m:
            if person_idx == len(mtimetable):
                return person_idx-1, m - shuttle_cnt
            if mtimetable[person_idx] > cur:
                break
            shuttle_cnt += 1
            person_idx += 1
        
        cur += t
    return person_idx-1, m - shuttle_cnt
def solution(n : int, t : int, m : int, timetable : List[str]):
    # timetable sort
    mtimetable = sorted(list(map(lambda x: hour_to_min(x), timetable)))
    
    last_person, remain_seats = find_last_person(n, m, t, mtimetable)
    # 마지막에 탄 사람의 셔틀 자리가 남아있다면
    if remain_seats:
        return min_to_hour(hour_to_min("09:00") + (t*(n-1)))
    # 셔틀 자리가 없다면
    else:
        return min_to_hour(mtimetable[last_person]-1)
    