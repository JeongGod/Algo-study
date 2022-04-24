from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def show():
	for i in range(r):
		for j in range(c):
			print(Map[i][j], end = '')
		if(i != r-1):
			print()

def shoot(dir, x):
	if(dir == True): # 왼쪽에서 오른쪽
		for i in range(0, c):
			if(Map[x][i] == 'x'):
				Map[x][i] = '.'
				return (x, i)
	else:
		for i in range(c-1, -1, -1):
			if(Map[x][i] == 'x'):
				Map[x][i] = '.'
				return (x, i)
	return False

def check(x, y):
	ret = []
	for d in range(4):
		nx = x + dx[d]
		ny = y + dy[d]
		if not (0 <= nx < r and 0 <= ny < c):
			continue 
		if(Map[nx][ny] == 'x'):
			ret.append((nx, ny))
	return ret
def hide(arr):
	for el in arr:
		x, y = el[0], el[1]
		Map[x][y] = '.'
	return 
def bfs(x, y):
	visited = [[0 for _ in range(c)] for _ in range(r)]
	if(Map[x][y] == '.'):
		return False
	lump =[[x,y]]
	q = deque()
	q.append((x, y))
	visited[x][y] = 1
	Map[x][y] = '.'
	while(q):
		x, y = q.popleft()
		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]
			if not (0 <= nx < r and 0 <= ny < c):
				continue
			if( Map[nx][ny] != 'x' or visited[nx][ny] != 0):
				continue
			Map[nx][ny] = '.'
			lump.append([nx, ny])
			visited[nx][ny] = 1
			q.append((nx, ny))
	return lump

def fall(lump):
	hide(lump)
	for el in lump:
		x, y = el[0], el[1]
		nx = x + 1
		ny = y
		if(nx >= r):
			for el in lump:
				Map[el[0]][el[1]] = 'x'
			return False
		if(Map[nx][ny] == '.'):
			continue
		else:
			for el in lump:
				Map[el[0]][el[1]] = 'x'
			return False
	
	for el in lump:
		el[0] += 1
		Map[el[0]][el[1]] = 'x'
	return True

# input
r, c = map(int,input().split())
Map = []
for _ in range(r):
	Map.append(list(input()))

n = int(input())
heightarr = list(map(int,input().split()))
for i in range(n):
	lumpall = []
	height = heightarr[i]
	if(i % 2 == 0): # 짝수 : 왼쪽에서 오른쪽
		broken = shoot(True, r - height)
	else: # 홀수 : 오른쪽에서 왼쪽
		broken = shoot(False, r - height)
	# 부순게 없었을 때
	if(broken == False):
		continue
	else:
		# 박살난 블럭의 상하좌우를 검사하여 덩어리 추출
		connected = check(broken[0], broken[1])
		for el in connected:
			arr = bfs(el[0], el[1])
			if(arr == False):
				continue
			else:
				lumpall.append(arr)
		# 한 덩어리도 더이상 못 움직일 때 까지
		flag = True
		while(flag):
			flag = False
			for el in lumpall:
				if(True == fall(el)):
					flag = True
					# show()
					# print()
	# print(i)
	# show()
	# print()
show()					
			
	