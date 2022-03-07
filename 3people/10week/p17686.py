def solution(files):
  answer = []
  for init, f in enumerate(files):
    idx = []
    for i in range(len(f)):
      if f[i].isdigit():
        if not idx or idx[-1] + 1 == i:
          idx.append(i)
        else:
          break
    answer.append([f[:idx[0]], f[idx[0]:idx[-1]+1], f[idx[-1]+1:], init])
  answer.sort(key=lambda x: (x[0].lower(), int(x[1]), x[3]))
  for a in answer:
    a.pop()
  answer = [''.join(map(str, a)) for a in answer]
  return answer