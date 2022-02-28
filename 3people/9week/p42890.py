from itertools import combinations

def solution(relation):
  answer = 0
  r = [el for el in zip(*relation)]
  cand = []
  for i in range(1, len(r) + 1):
    combi = list(combinations([r[i] for i in range(len(r))], i))
    combi_idx = list(combinations([i for i in range(len(r))], i))
    for j in range(len(combi)):
      group = []
      for k in range(len(combi[j][0])):
        group.append(tuple(combi[j][l][k] for l in range(len(combi[j]))))
      if len(group) == len(set(group)):
        cand.append(set(combi_idx[j]))
  for i in range(len(cand)):
    flag = True
    for j in range(i):
      if cand[j].issubset(cand[i]):
        flag = False
        break
    if flag:
      answer += 1
  return answer