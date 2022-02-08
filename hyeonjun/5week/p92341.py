import datetime
import math

dateformat = '%H:%M'
END_OF_THE_DAY = datetime.datetime.strptime('23:59', dateformat)


def solution(fees, records):
    answer = []
    accumulated_time = {}
    parking_lot = {}

    default_time, default_fee, unit_time, unit_fee = fees

    for record in records:
        time, number, in_out = record.split()
        if in_out == 'IN':
            parking_lot[number] = datetime.datetime.strptime(time, dateformat)
        else:
            start_time = parking_lot[number]
            end_time = datetime.datetime.strptime(time, dateformat)
            parking_time = (end_time-start_time).seconds/60
            del parking_lot[number]

            if number in accumulated_time:
                accumulated_time[number] += parking_time
            else:
                accumulated_time[number] = parking_time

    for remaining in parking_lot:
        start_time = parking_lot[remaining]
        parking_time = (END_OF_THE_DAY-start_time).seconds/60

        if remaining in accumulated_time:
            accumulated_time[remaining] += parking_time
        else:
            accumulated_time[remaining] = parking_time

    for car in accumulated_time:
        if accumulated_time[car] <= default_time:
            accumulated_time[car] = default_fee
        else:
            accumulated_time[car] = default_fee + \
                math.ceil(
                    (accumulated_time[car] - default_time)/unit_time)*unit_fee

    tmp = sorted(accumulated_time.items())
    for elm in tmp:
        answer.append(elm[1])

    return answer
