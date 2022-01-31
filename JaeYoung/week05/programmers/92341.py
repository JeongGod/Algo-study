import math
from typing import Dict, List


def calc_time(in_time: str, out_time: str) -> int:
    in_hour, in_min = in_time.split(":")
    out_hour, out_min = out_time.split(":")

    past_hour: int = int(out_hour) - int(in_hour)
    past_min: int = int(out_min) - int(in_min)

    return past_hour * 60 + past_min


def solution(fees: List[int], records: List[str]) -> List[int]:
    answer: List[int] = []
    cars: Dict[str, List[str]] = dict()
    for record in records:
        time, car, _ = record.split(" ")
        if car in cars:
            cars[car].append(time)
        else:
            cars[car] = [time]

    for car, park_times in cars.items():
        total_time: int = 0
        total_fee: int = 0
        if len(park_times) % 2 == 0:  # 입출차 기록이 짝수인 경우 -> 결국 출차함
            for i in range(0, len(park_times)-1, 2):
                total_time += calc_time(park_times[i], park_times[i+1])
        else:  # 입출차 기록이 홀수인 경우 -> 23:59분에 출차한걸로 간주
            if len(park_times) > 1:
                for i in range(0, len(park_times)-1, 2):
                    total_time += calc_time(park_times[i], park_times[i+1])
            total_time += calc_time(park_times[-1], "23:59")

        total_fee += fees[1]
        if total_time > fees[0]:
            total_fee += (math.ceil((total_time - fees[0])/fees[2])) * fees[3]

        answer.append([car, total_fee])

    answer = sorted(answer, key=lambda x: x[0])
    answer = list(list(zip(*answer))[1])

    return answer
