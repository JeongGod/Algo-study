
# 온도가 조절됨
# 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
# 초콜릿을 하나 먹는다.
# 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.
from collections import deque
dx = [0,0,-1,1]
dy = [1,-1,0,0]
nextd = [
	[[-1, 1], [0, 1], [1, 1]], # 오른쪽
	[[-1, -1], [0, -1], [1, -1]], # 왼쪽
	[[-1, -1], [-1, 0], [-1, 1]], #위
	[[1, -1], [1, 0], [1, 1]] # 아래
]

def showmap():
	print()
	for i in range(R):
		for j in range(C):
			print(Map[i][j], end = ' ')
		print()
	print() 

def blow():
	for blower in blowers:
		x, y, d = blower
		nx = x + dx[d]
		ny = y + dy[d]
		if not (0 <= nx < R and 0 <= ny < C):
			continue
		power = 5
		visited = [[False for _ in range(C)] for _ in range(R)]
		Map[nx][ny] += power
		visited[nx][ny] = True
		q = deque()
		q.append([nx, ny, power -1])
		while q:
			x, y, nowpower = q.popleft()
			if nowpower == 0:
				continue

			for dir in nextd[d]:
				nx = x + dir[0]
				ny = y + dir[1]
				if not (0 <= nx < R and 0 <= ny < C):
					continue
				if(visited[nx][ny] == True):
					continue
				manhdist = abs(x - nx) + abs(y -ny)
				# 맨허튼 거리 1
				if(manhdist == 1):
					if((x, y, nx, ny) in wall):
						continue
				else: #꺽어서 가야할 때 중간 지점을 알아야댐
					if(d == 0 or d == 1):
						midx, midy = x+dir[0], y
					else:
						midx, midy = x, y+dir[1]
					if((x, y, midx, midy) in wall or (nx, ny, midx, midy) in wall):
						continue
				Map[nx][ny] += nowpower
				visited[nx][ny] = True
				q.append([nx, ny, nowpower -1])

def regulate():
	temperature =  [[0 for _ in range(C)] for _ in range(R)]

	for x in range(R):
		for y in range(C):
			for d in range(4):
				nx = x + dx[d]
				ny = y + dy[d]
				if not (0 <= nx < R and 0 <= ny < C):
					continue
				if((x, y, nx, ny) in wall):
					continue
				if(Map[x][y] > Map[nx][ny]): # 온도 변경이 일어나야하면
					tmp = (Map[x][y] - Map[nx][ny])//4
					temperature[x][y] -= tmp
					temperature[nx][ny] += tmp
	for x in range(R):
		for y in range(C):
			Map[x][y] += temperature[x][y]

def checktemp():
	for x, y in NeedCheck:
		if(Map[x][y] < K):
			return False
	return True

def lowtemp():
	for i in range(0, C):
		if(Map[0][i] > 0):
			Map[0][i] -= 1
		if(Map[R-1][i] > 0):
			Map[R-1][i] -= 1
	for i in range(1, R-1):
		if(Map[i][0] > 0):
			Map[i][0] -= 1
		if(Map[i][C-1]):
			Map[i][C-1] -= 1

# 입력
answer = 0
R, C, K = map(int,input().split())
Map = []
for _ in range(R):
	Map.append(list(map(int,input().split())))
NeedCheck = []
blowers = [] # [i, j, d] , 0 == 오른쪽 -> 반시계 방향으로 인덱싱 진행
for i in range(R):
	for j in range(C):
		if(Map[i][j] == 0): #빈칸
			continue

		elif(Map[i][j] == 5): # 조사가 필요한 위치 발견
			NeedCheck.append([i,j]) # 조사가 필요한 위치 저장
			Map[i][j] = 0 # 빈칸 취급

		else: # 온풍기 설치
			blowers.append([i, j, Map[i][j]- 1]) # d 자릿수 맞춰주기위한 -1
			Map[i][j] = 0 # 빈칸 취급

wall = set() # 벽 (x1, y1, x2, y2 ), t == 0 -> (x-1, y) , t == 1 -> (x, y+1)
W = int(input())
for _ in range(W):
	x, y ,t = map(int,input().split())
	x = x-1
	y = y-1
	if(t == 0):
		wall.add((x, y, x-1, y))
		wall.add((x-1, y, x, y))
	else:
		wall.add((x, y, x, y+1))
		wall.add((x, y+1, x, y))

while True:
	# 집에 있는 모든 온풍기에서 바람이 한 번 나옴
	blow()
	# 온도가 조절됨
	regulate()
	lowtemp()
	answer += 1
	if(checktemp()):
		break
	if(answer > 100):
		break
# showmap()
print(answer)