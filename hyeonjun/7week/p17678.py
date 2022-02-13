from datetime import timedelta
from datetime import datetime


def str_to_time(given_str):
    return datetime.strptime(given_str, '%H:%M')


def time_to_str(given_time):
    return given_time.strftime('%H:%M')


def solution(n, t, m, timetable):
    timetable.sort()
    unit_time = timedelta(minutes=t)
    start_time = str_to_time('09:00') - unit_time

    bus_table = []
    for _ in range(n):
        start_time += unit_time
        bus_table.append(start_time)

    idx = 0
    for bus in bus_table:
        limit = m
        for user in timetable[idx:]:
            if str_to_time(user) <= bus:
                if bus == bus_table[-1] and limit == 1:
                    return time_to_str(str_to_time(user) - timedelta(minutes=1))
                limit -= 1
                idx += 1
                if not limit:
                    break
            else:
                break

    return time_to_str(bus_table[-1])
