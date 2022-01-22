from itertools import permutations

def makeList(exp, op):
  arr = []
  temp = ''
  for e in exp:
    if e in op:
      arr.append(temp)
      arr.append(e)
      temp = ''
    else:
      temp += e
  arr.append(temp)
  return arr

def solution(expression):
  operations = ['+', '-', '*']
  maxx = -1e9
  for op in permutations(operations, 3):
    arr = makeList(expression, op)
    for i in range(len(op)):
      p = 0
      while p < len(arr):
        if op[i] == arr[p]:
          arr[p-1] = str(eval(arr[p-1] + op[i] + arr[p+1]))
          arr.pop(p)
          arr.pop(p)
        else:
          p += 1
    res = abs(int(arr[0]))
    maxx = max(maxx, res)
  return maxx