def solution(begin, target, words):
  if target not in words:
    return 0
  visited = [0] * len(words)
  s = [begin]
  answer = 0
  while s:
    top = s.pop()
    if top == target:
      return answer
    for i in range(len(words)):
      cnt = 0
      for j in range(len(words[i])):
        if words[i][j] != top[j]:
          cnt += 1
      if cnt == 1:
        if visited[i] == 1:
          continue
        visited[i] = 1
        s.append(words[i])
  answer += 1
  return answer