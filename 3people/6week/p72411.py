from itertools import combinations
from collections import Counter

def solution(orders, course):
  answer = []
  for c in course:
    temp = []
    for order in orders:
      combi = combinations(sorted(order), c)
      temp += combi
    counter = Counter(temp)
    if len(counter) != 0 and max(counter.values()) != 1:
      for cnt in counter:
        if counter[cnt] == max(counter.values()):
          answer.append("".join(cnt))
  return sorted(answer)