from copy import deepcopy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def MoveFish(sharkx, sharky,Map, fish):
	for i in range(16):
		if(fish[i] != None):
			x = fish[i][0] # 움직일 물고기 좌표
			y = fish[i][1]
			for d in range(8):
				nx = x + dx[Map[x][y][1]]
				ny = y + dy[Map[x][y][1]]
				if not (0 <= nx < 4 and 0 <= ny < 4 ):
					Map[x][y][1] = (Map[x][y][1]+1) % 8
					continue
				if(nx == sharkx and ny == sharky):
					Map[x][y][1] = (Map[x][y][1]+1) % 8
					continue
				if(Map[nx][ny] == None):
					fish[i] = [nx, ny] # 물고기 좌표 바꾸기
					Map[nx][ny], Map[x][y] = Map[x][y], Map[nx][ny] # 맵상 물고기 위치 바꾸기
					break
				fish[Map[nx][ny][0]], fish[i] = [x, y], [nx, ny] # 물고기 좌표 바꾸기
				Map[nx][ny], Map[x][y] = Map[x][y], Map[nx][ny] # 맵상 물고기 위치 바꾸기
				break

def dfs(sharkx, sharky, d, cnt,Map, fish):
	global mx
	# print(cnt, "현재점수")
	MoveFish(sharkx,sharky,Map, fish) #상어 위치를 제외한 자리로 움직이기 위해 상어 좌표를 인자로 받아감
	# 상어 움직이기
	while True:
		nx = sharkx + dx[d]
		ny = sharky + dy[d]
		if not(0 <= nx < 4 and 0 <= ny < 4): # 범위 벗어나면 종료
			mx = max(mx, cnt)
			return
		if(Map[nx][ny] == None): #물고기가 없는 칸에 정착은 불가능하지만 이동 경로로 사용은 가능
			sharkx, sharky = nx, ny
			continue
		
		copy_Map = deepcopy(Map)
		copy_fish = deepcopy(fish)
		next_d = Map[nx][ny][1]
		save_fish = fish[Map[nx][ny][0]]
		fish[Map[nx][ny][0]] = None # 물고기 먹기
		get_point = Map[nx][ny][0] + 1
		Map[nx][ny] = None
		# print(get_point, "이거 먹음")
		dfs(nx,ny,next_d, cnt+get_point,Map, fish)
		Map = copy_Map
		fish = copy_fish
		# Map[nx][ny] = [get_point-1,next_d]
		# fish[Map[nx][ny][0]] = save_fish # 물고기 불러오기
		sharkx = nx
		sharky = ny
		
		
		


Map = [[ None for _ in range(4)] for _ in range(4)]
fish = [[] for _ in range(16)]
for i in range(4):
	temp = list(map(int, input().split()))
	for j in range(0,8,2):
		fish[temp[j]-1] = [i, j//2] # 물고기 좌표
		Map[i][j//2] = [temp[j]-1,temp[j+1]-1] # 물고기 번호와 방향 빼기 1 저장

# 공통사항 상어가 (0, 0) 물고기를 먹는다
global mx
mx = 0
cnt = 0
eatfish = Map[0][0] # (0,0) 물고기
Map[0][0] = None
d = eatfish[1] # 먹은 물고기의 방향 가져가기
cnt += eatfish[0] + 1
fish[eatfish[0]] = None
dfs(0, 0, d, cnt, Map, fish) # 상어의 x y 좌표 및 방향, 현재 점수
print(mx)