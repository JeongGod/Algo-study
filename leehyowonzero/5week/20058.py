from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def showmap():
	for i in range(size):
		for j in range(size):
			print(Map[i][j], end = ' ')
		print()
	print()

def SwapBox(x, y, l):
	q = deque()
	for i in range(x, x+l):
		for j in range(y, y+l):
			q.append(Map[i][j])

	for j in range(y+l-1, y-1, -1):
		for i in range(x, x+l):
			Map[i][j] = q.popleft()

def firestorm(l):
	for i in range(0,size,l):
		for j in range(0, size, l):
			SwapBox(i, j, l)

def meltdow():
	meltingMap = [[0 for _ in range(size)] for _ in range(size)]
	for x in range(size):
		for y in range(size):
			cnt = 0
			for d in range(4):
				nx = x + dx[d]
				ny = y + dy[d]
				if not (0<=nx <size and 0<=ny<size):
					continue
				if(Map[nx][ny] > 0):
					cnt += 1
			if(cnt < 3):
				meltingMap[x][y] += 1
	for x in range(size):
		for y in range(size):
			if(Map[x][y] > 0):
				Map[x][y] -= meltingMap[x][y]

def bfs(x, y):
	visited[x][y] = True
	cnt = 1
	q = deque()
	q.append([x, y])
	while q :
		x, y = q.popleft()
		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]
			if not (0<=nx <size and 0<=ny<size):
				continue
			if(visited[nx][ny] == True):
				continue
			if(Map[nx][ny] > 0):
				q.append([nx, ny])
				cnt += 1
				visited[nx][ny] = True
	return cnt
N, Q = map(int,input().split())
Map = []
size = 2**N
for _ in range(size):
	Map.append(list(map(int,input().split())))

MagicLevel = list(map(int,input().split()))

for i in range(Q):
	firestorm(2**MagicLevel[i])
	meltdow()

print(sum(list(sum(Map[i]) for i in range(size)))) # 남아있는 얼음의 합

# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
answer = 0
visited = [[False for _ in range(size)] for _ in range(size)]
for x in range(size):
	for y in range(size):
		if(visited[x][y] == False and Map[x][y] > 0):
			answer = max(answer, bfs(x, y))
print(answer)