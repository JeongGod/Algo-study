def solution(info, query):
  answer = [0] * len(query)
  for i in range(len(info)):
    info[i] = info[i].split()
  for i in range(len(query)):
    query[i] = query[i].split()
    for j in range(3):
      query[i].remove('and')
  for i in range(len(query)):
    for j in range(len(info)):
      for k in range(5):
        if query[i][k] == '-':
          continue
        elif k == 4:
          if int(query[i][k]) <= int(info[j][k]):
            answer[i] += 1
        elif query[i][k] != info[j][k]:
          break
  return answer

from itertools import combinations
from bisect import bisect_left

def solution(info, query):
  answer = []
  dic = {}
  for i in info:
    temp = i.split()
    condition = temp[:-1]
    score = int(temp[-1])
    for i in range(5):
      for c in list(combinations([0,1,2,3], i)):
        cond_copy = condition.copy()
        for idx in c:
          cond_copy[idx] = '-'
        key = ''.join(cond_copy)
        if key in dic:
          dic[key].append(score)
        else:
          dic[key] = [score]

  for value in dic.values():
    value.sort()

  for q in query:
    query_list = []
    for s in q.split():
      if s == 'and':
        continue
      query_list.append(s)

    target = int(query_list[-1])
    query_key = ''.join(query_list[:-1])
    if query_key in dic:
      cand = dic[query_key]
      index = bisect_left(cand, target)
      answer.append(len(cand) - index)
    else:
      answer.append(0)
  return answer