import math

def calc_min(before, after):
  b = list(map(int, before.split(':')))
  a = list(map(int, after.split(':')))
  if b[1] > a[1]:
    return ((a[0] - b[0] - 1) * 60) + (a[1] - b[1] + 60)
  else:
    return ((a[0] - b[0]) * 60) + (a[1] - b[1])
    
def calc_time(info):
  l = len(info)
  time = 0
  if l % 2 == 1:
    info.append((('23:59', 'OUT')))
  for i in range(0, l, 2):
    time += calc_min(info[i][0], info[i+1][0])
  return time

def calc_fees(fees, time):
  for i, t in enumerate(time):
    if t <= fees[0]:
      time[i] = fees[1]
    else:
      time[i] = fees[1] + (math.ceil((t - fees[0]) / fees[2]) * fees[3])
            
def solution(fees, records):
  answer = []
  records = [r.split() for r in records]
  info = {}
  records.sort(key=lambda x: x[1])
  for r in records:
    if r[1] not in info:
      info[r[1]] = []
    info[r[1]].append((r[0], r[2]))
  for _, values in info.items():
    answer.append(calc_time(values))
  calc_fees(fees, answer)
      
  return answer