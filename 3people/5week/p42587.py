def solution(priorities, location):
  answer = 0
  p = [el for el in enumerate(priorities)]
  while True:
    top = p.pop(0)
    if p == []:
      answer += 1
      break
    if top[1] < max(p, key=lambda x: x[1])[1]:
      p.append(top)
    else:
      answer += 1
      if top[0] == location:
        return answer
  return answer