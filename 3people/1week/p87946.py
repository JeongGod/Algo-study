from itertools import permutations

def solution(k, dungeons):
  answer = -1
  for el in permutations(dungeons):
    fatigue = k
    cnt = 0
    for d in el:
      if d[0] <= fatigue:
          fatigue -= d[1]
          cnt += 1
      else:
          break
      answer = max(answer, cnt)
  return answer