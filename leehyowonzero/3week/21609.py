from collections import deque
import copy 

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def showmap():
	for i in range(N-1,-1, -1):
		for j in range(N):
			print(Map[i][j], end = ' ')
		print()
	print()
def zeros(arr):
	ret = 0
	for x, y in arr:
		if(Map[x][y] == 0):
			ret += 1
	return ret
def FindAndRemove():
	ret = []
	visited = [[False for _ in range(N)] for _ in range(N)]
	for i in range(N):
		for j in range(N):
			if(Map[i][j] == None):
				continue
			if(Map[i][j] != -1 and Map[i][j] != 0): # 색이 있는 방문 기록이 없는 블록을 밟았을 때
				q = deque()
				candiBlocks = []
				candizero = 0
				candiBlockColor = Map[i][j]
				q.append([i, j])
				candiBlocks.append([i,j])
				visited[i][j] = True

				while q:
					x, y = q.popleft()
					for d in range(4):
						nx = x + dx[d]
						ny = y + dy[d]
						if not (0 <= nx < N and 0<= ny < N):
							continue
						if(visited[nx][ny] == True):
							continue
						if(Map[nx][ny] == candiBlockColor or Map[nx][ny] == 0):
							q.append([nx, ny])
							visited[nx][ny] = True
							candiBlocks.append([nx,ny])
							if(Map[nx][ny] == 0):
								candizero += 1
				for x, y in candiBlocks:
					if(Map[x][y] == 0):
						visited[x][y] = False
				if(len(candiBlocks) == len(ret)):
					if(candizero >= zeros(ret)):
						ret = candiBlocks
				elif(len(candiBlocks) > len(ret)):
					ret = candiBlocks
	return ret 

def gravity():
	for j in range(N):
		q = deque()
		flooridx = N-1
		for i in range(N-1, -1, -1):
			if(Map[i][j] == None):
				continue
			elif(Map[i][j] == -1):
				while q:
					Map[flooridx][j] = q.popleft()
					flooridx -= 1
				flooridx = i - 1
			else:
				q.append(Map[i][j])
				Map[i][j] = None
		while q:
			Map[flooridx][j] = q.popleft()
			flooridx -= 1

def rotateleft():
	global Map
	nextMap = [[None for _ in range(N)] for _ in range(N)]
	for j, col in enumerate(Map):
		for i, el in enumerate(col):
			nextMap[N-1-i][j] = el
	Map = copy.deepcopy(nextMap)



N, M = map(int,input().split())
Map = []
for _ in range(N):
	Map.append(list(map(int,input().split())))
score = 0
while True:
	# 크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
	RemovedBlocks = FindAndRemove()
	# 오늘은 이 게임에 오토 플레이 기능을 만드려고 한다. 오토 플레이는 다음과 같은 과정이 블록 그룹이 존재하는 동안 계속해서 반복되어야 한다.
	if (len(RemovedBlocks) < 2):
		break
	# 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.
	for x, y in RemovedBlocks:
		Map[x][y] = None # 빈 블럭은 None 표시
	score += len(RemovedBlocks)**2 
	# 격자에 중력이 작용한다.
	gravity()
	# 격자가 90도 반시계 방향으로 회전한다.
	rotateleft()
	# 다시 격자에 중력이 작용한다.
	gravity()
	# showmap()
print(score)