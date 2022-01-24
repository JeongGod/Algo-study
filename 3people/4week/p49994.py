def solution(dirs):
  dir = {'U': (0,1), 'D': (0,-1), 'R': (1,0), 'L': (-1,0)}
  visited = set()
  x, y = 0, 0
  for d in dirs:
    nx = x + dir[d][0]
    ny = y + dir[d][1]
    if -5 <= nx <= 5 and -5 <= ny <= 5:
      visited.add(((x,y),(nx,ny)))
      visited.add(((nx,ny),(x,y)))
      x = nx
      y = ny
  return len(visited) // 2

def solution(dirs):
  dir = {'U': (0,1), 'D': (0,-1), 'R': (1,0), 'L': (-1,0)}
  visited = []
  x, y = 0, 0
  for d in dirs:
    nx = x + dir[d][0]
    ny = y + dir[d][1]
    if -5 <= nx <= 5 and -5 <= ny <= 5:
      if ((x,y), (nx,ny)) not in visited and ((nx,ny), (x,y)) not in visited:
        visited.append(((x,y), (nx,ny)))
      x = nx
      y = ny
  return len(visited)