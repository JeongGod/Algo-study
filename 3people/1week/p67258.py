def solution(gems):
  ans = []
  s = list(set(gems))
  dic = {}
  front = 0
  rear = 0
  shortest = len(gems) + 1
  while rear < len(gems):
    if gems[rear] not in dic:
      dic[gems[rear]] = 1
    else:
      dic[gems[rear]] += 1
    rear += 1
    
    if len(dic) == len(s):
      while front < rear:
        if dic[gems[front]] > 1:
          dic[gems[front]] -= 1
          front += 1
        elif shortest > rear - front:
          shortest = rear - front
          ans = [front+1, rear]
          break
        else:
          break
                    
  return ans