# 틀림
def dfs(start, tickets, arr):
  global answer
  for i in range(len(tickets)):
    if tickets == []:
      answer = arr
      return
    if start == tickets[i][0]:
      start = tickets[i][1]
      arr.append(start)
      tickets.pop(i)
      dfs(start, tickets, arr)

def solution(tickets):
  global answer
  tickets.sort(key=lambda x: x[1]) 
  dfs('ICN', tickets, ['ICN'])
  return answer

# 맞음
def dfs(tickets, start, used):
  for i in range(len(tickets)):
    if tickets[i][0] == start and i not in used:
      used.append(i)
      dfs(tickets, tickets[i][1], used)
      if len(tickets) == len(used):
        return
      else:
        used.pop()

def solution(tickets):
  answer = ['ICN']
  tickets.sort(key=lambda x: (x[0], x[1]))
  used = []
  dfs(tickets, 'ICN', used)
  for i in used:
    answer.append(tickets[i][1])
  return answer