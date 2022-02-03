import math


def calc(exceed_time : int) -> int:
    # 초과하지 않았다면
    if exceed_time <= 0:
        return 0
    return math.ceil(exceed_time / i_time) * i_price

def hour_to_minute(time : str):
    hour, minute = map(int, time.split(":"))
    return hour*60 + minute

def solution(fees, records):
    global b_time, b_price, i_time, i_price
    """
    1. 입차된 후에 출차 내역이 없다면 23:59분에 출차한 것으로
    2. 기본 요금, 기본 요금 + 단위 시간(올림) * 단위 요금
    차량 번호가 작은 자동차부터 청구할 주차 요금
    """
    answer = []
    b_time, b_price, i_time, i_price = fees
    cars = dict()
    for time, car, com in map(lambda x:x.split(), records):
        if com == "IN":
            target = cars.get(car)
            # 처음 차량이 들어왔다면
            if target is None:
                cars[car] = [hour_to_minute(time), 0, True]
                continue
            # 다시 들어온다면
            target[0] = hour_to_minute(time)
            target[2] = True
        else:
            target = cars.get(car)
            target[1] += hour_to_minute(time) - target[0]
            target[2] = False
            
    for car in sorted(cars.keys()):
        # 출차하지 않은 경우
        target = cars[car]
        if target[2] == 1:
            target[1] += hour_to_minute("23:59") - target[0]
        # 계산
        answer.append(b_price + calc(target[1] - b_time))
        
    return answer
