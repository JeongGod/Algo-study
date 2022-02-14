def solution(n, t, m, timetable):
  answer = ''
  timetable = sorted([int(t[:2]) * 60 + int(t[3:]) for t in timetable])
  bus_timetable = [540 + i*t for i in range(n)]
  
  for i in range(len(bus_timetable)-1):
    for _ in range(m):
      if timetable[0] <= bus_timetable[i]:
        timetable.pop(0)
      else:
        break
          
  last_bus = bus_timetable[-1]
  in_bus = []
  for time in timetable:
    if time <= last_bus:
      in_bus.append(time)
    if len(in_bus) == m:        
      break
  answer = last_bus if len(in_bus) < m else max(in_bus) -1
  return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)