from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(posx, posy, size):
	global sharkpos, sharksize, fishcnt, noweat, answer
	candi = []
	visited = [[False for _ in range(n)] for _ in range(n)]
	q = deque()
	q.append([0, posx, posy])
	visited[posx][posy] = True
	while q :
		nowturn = len(q)
		flag = False
		for _ in range(nowturn):
			dist, x, y = q.popleft()
			for d in range(4):
				nx = x + dx[d]
				ny = y + dy[d]
				if not (0 <= nx < n and 0 <= ny < n):
					continue
				if(visited[nx][ny] == True):
					continue
				if(0 < Map[nx][ny] < size):
					flag = True
					candi.append([dist+1, nx, ny ]) # 거리, 좌표, 사이즈
					visited[nx][ny] = True
					q.append([dist+1, nx, ny])

				elif(Map[nx][ny] == 0 or Map[nx][ny] ==  size):
					visited[nx][ny] = True
					q.append([dist+1, nx, ny])
				else:
					visited[nx][ny] = True
		if(flag):
			break

	if(candi):
		candi.sort()
		eatfish = candi[0] # 제일 알맞은 물고기 선택
		Map[eatfish[1]][eatfish[2]] = 0
		fishcnt -= 1
		answer += eatfish[0]
		sharkpos = eatfish[1:]
		noweat += 1
		return True

	return False
	

n = int(input())
Map = []
for _ in range(n):
	Map.append(list(map(int,input().split())))
answer = 0
sharksize = 2
noweat = 0
fishcnt = 0
# 아기상어 위치 및 물고기 수 찾기
for i in range(n):
	for j in range(n):
		if(1 <= Map[i][j] <= 6):
			fishcnt += 1

		elif(Map[i][j] == 9):
			sharkpos = i, j
			Map[i][j] = 0
			
while True:
	if(fishcnt == 0): # 물고기 없으면 끝
		break
		
	if not(bfs(sharkpos[0], sharkpos[1], sharksize)): # 먹을 물고기가 있는지 판단
		break
	if(sharksize == noweat): # 물고기 승급
		sharksize += 1
		noweat = 0
print(answer)