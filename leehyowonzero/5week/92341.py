from collections import defaultdict
import math

def convert(time):
    hours, minute = map(int, time.split(':'))
    return hours*60 + minute

def solution(fees, records):
    answer = defaultdict(int)
    fees[0] # 기본 시간
    fees[1] # 기본 요금
    fees[2] # 단위 시간
    fees[3] # 단위 요금
    lasttime = 1439
    parkinglot = dict()
    for record in records:
        time, number, state = record.split(' ')
        convertedtime = convert(time)
        if(state == "IN"):
            parkinglot[number] = convertedtime
        else: # OUT
            answer[number] += convertedtime - parkinglot.pop(number)
    for number in parkinglot:
        answer[number] += lasttime - parkinglot[number]
    for el in answer:
        if(answer[el] > fees[0]):
            answer[el] = fees[1] + math.ceil(((answer[el] - fees[0]) / fees[2])) * fees[3]
        else:
            answer[el] = fees[1]
    return list( x[1] for x in sorted(answer.items()))