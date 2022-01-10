def vp(p):
  stack = []
  for i in p:
    if i == '(':
      stack.append(i)
    else:
      if not stack:
        return False
      else:
        stack.pop()
  return True

def divide(p):
  l = 0
  r = 0
  
  for i in range(len(p)):
    if p[i] == '(':
      l += 1
    else:
      r += 1
    if l == r:
      return p[:i+1], p[i+1:] 
    

def solution(p):
  answer = ''
  # 1
  if not p:
    return ""
  # 2
  u, v = divide(p)
  # 3
  if vp(u):
    return u + solution(v)
  # 4
  else:
    # 4-1
    answer = '('
    # 4-2
    answer += solution(v)
    # 4-3
    answer += ')'
    # 4-4
    for i in u[1:len(u)-1]:
      if i == '(':
        answer += ')'
      else:
        answer += '('
  return answer