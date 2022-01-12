from collections import deque

def vp(p):
  stack = []
  for i in p:
    if i in ['(', '{', '[']:
      stack.append(i)
    else:
      if not stack:
        return False
      else:
        if stack[len(stack) - 1] == '(':
          if i == ')':
            stack.pop()
          else:
            return False
        elif stack[len(stack) - 1] == '{':
          if i == '}':
            stack.pop()
          else:
            return False
        elif stack[len(stack) - 1] == '[':
          if i == ']':
            stack.pop()
          else:
            return False
  return True

def solution(s):
  answer = 0
  deq = deque()
  if len(s) % 2 != 0:
    return 0
  for el in s:
    deq.append(el)
  if vp(deq):
    answer += 1
  for _ in range(len(deq) - 1):
    deq.append(deq.popleft())
    if vp(deq):
      answer += 1
  return answer