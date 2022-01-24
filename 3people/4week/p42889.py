def solution(N, stages):
  answer = []
  fail = [[0,0] for _ in range(N)]
  for stage in stages:
    if stage == N+1:
      for i in range(stage-1):
        fail[i][1] += 1   
    else:
      for i in range(stage):
        fail[i][1] += 1
      fail[stage-1][0] += 1
  for idx, f in enumerate(fail):
    if f[0] == 0 or f[1] == 0:
      answer.append((idx+1, 0))
    else:
      answer.append((idx+1, (f[0] / f[1])))
  answer = sorted(answer, key=lambda x: (-x[1], x[0]))
  answer = [a[0] for a in answer]
  return answer