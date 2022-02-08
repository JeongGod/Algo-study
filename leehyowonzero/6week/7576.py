from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def check():
	for i in range(m):
		for j in range(n):
			if(Map[i][j] == 0):
				return False
	return True

n, m = map(int,input().split())
Map = []
for _ in range(m):
	Map.append(list(map(int,input().split())))

tomato = []
for i in range(m):
	for j in range(n):
		if(Map[i][j] == 1):
			tomato.append([i, j])
answer = 0
if(check()): # 처음부터 조건 만족
	print(answer)
	exit(0)

if(len(tomato) == 0): # 만약 토마토가 없엉
	print(-1)
	exit(0)
	
q = deque(tomato)
while q:
	answer += 1
	nowturn = len(q)
	flag = False
	for _ in range(nowturn):
		x, y = q.popleft()
		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]
			if not (0 <= nx < m and 0 <= ny < n):
				continue
			if(Map[nx][ny] != 0):
				continue
			flag = True
			Map[nx][ny] = 1
			q.append([nx, ny])
	if not(flag): # 토마토가 익힐 수 없어용
		print(-1)
		break
	if(check()):
		print(answer)
		break
