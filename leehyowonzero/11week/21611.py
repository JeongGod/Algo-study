import pprint
from collections import deque
blizzard_dx = [0,-1,1,0,0]
blizzard_dy = [0,0,0,-1,1]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
def Change_ball_by_one_dimension_Map(one_dimension_Map):
    new_one_dimension_Map = []
    ball_idx = -1
    ball_len = 0
    for i, el in enumerate(one_dimension_Map):
        if(el == 0):
            new_one_dimension_Map.append(ball_len)
            new_one_dimension_Map.append(ball_idx)
            break
        if(i == 0):
            ball_idx = el
            ball_len += 1
        else:
            if(el == ball_idx):
                ball_len += 1
            else:
                new_one_dimension_Map.append(ball_len)
                new_one_dimension_Map.append(ball_idx)
                ball_idx = el
                ball_len = 1
        if(i == len(one_dimension_Map) - 1): # 마지막 인덱스 예외처리
            new_one_dimension_Map.append(ball_len)
            new_one_dimension_Map.append(ball_idx)
    return new_one_dimension_Map
def boom_Map(one_dimension_Map):
    ball_idx = -1
    ball_len = 0
    flag = False
    for i, el in enumerate(one_dimension_Map):
        if(el == 0):
            if(ball_len >= 4):
                flag = True
                answer[ball_idx] += ball_len
                for j in range(i-1 ,i-1-ball_len, -1):
                    one_dimension_Map[j] = 0
            break
        if(ball_idx == -1): #최초
            ball_idx = el
            ball_len += 1
        else:
            if(el == ball_idx):
                ball_len += 1
            else:
                if(ball_len >= 4):
                    flag = True
                    answer[ball_idx] += ball_len
                    for j in range(i-1 ,i-1-ball_len, -1):
                        one_dimension_Map[j] = 0
                ball_idx = el
                ball_len = 1
        if(i == len(one_dimension_Map) - 1): # 마지막 인덱스 예외처리
            if(ball_len >= 4):
                flag = True
                answer[ball_idx] += ball_len
                for j in range(i-1 ,i-1-ball_len, -1):
                    one_dimension_Map[j] = 0
    return flag, one_dimension_Map
def change_Map(one_dimension_Map_pos, one_dimension_Map):
    global Map
    if(len(one_dimension_Map) > N*N-1):
        one_dimension_range = N*N-1
    else:
        one_dimension_range = len(one_dimension_Map)
    for i in range(one_dimension_range):
        Map[one_dimension_Map_pos[i][0]][one_dimension_Map_pos[i][1]] = one_dimension_Map[i]
    
def clean_Map():
    global Map
    for x in range(N):
        for y in range(N):
            Map[x][y] = 0
            
def Make_one_dimension_Map(Map, one_dimension_Map_pos): # 1차원 맵 만들기
    one_dimension_Map = []
    for x, y in one_dimension_Map_pos:
        if(Map[x][y] != 0): # 빈 공간은 바로 빼버리기
            one_dimension_Map.append(Map[x][y]) 
    return one_dimension_Map


N, M = map(int,input().split())
Map = []
for _ in range(N):
    Map.append(list(map(int,input().split())))
blizzard = []
for _ in range(M):
    blizzard.append(list(map(int,input().split()))) # blizzard[d, s] 방향 거리
sharkpos = [(N-1)//2, (N-1)//2]
answer = [0, 0, 0, 0]
realanswer = 0
# 1차원 맵 생성
one_dimension_Map_pos = [None for _ in range(N*N -1)]
startpos = sharkpos
nowpos = startpos
nowlen = 1
one_dimension_idx = 0
for i in range(1, N): # 모든 공간을 돌면서 구슬 수집
    if(i%2 == 1):
        for d in [(0,-1), (1,0)]:
            for _ in range(nowlen):
                nowpos = [nowpos[0] + d[0] , nowpos[1] + d[1]]
                one_dimension_Map_pos[one_dimension_idx] = nowpos
                one_dimension_idx += 1
    else:
        for d in [(0,1), (-1,0)]:
            for _ in range(nowlen):
                nowpos = [nowpos[0] + d[0] , nowpos[1] + d[1]]
                one_dimension_Map_pos[one_dimension_idx] = nowpos
                one_dimension_idx += 1
    nowlen += 1
for _ in range(N-1):
    nowpos = [nowpos[0] + dx[0] , nowpos[1] + dy[0]]
    one_dimension_Map_pos[one_dimension_idx] = nowpos
    one_dimension_idx += 1

    

for turn in range(M):
    # 블리자드 얼음파편 발사
    ice_dir , ice_range = blizzard[turn]
    for i in range(1, ice_range+1):
        Map[sharkpos[0] + blizzard_dx[ice_dir]*i][sharkpos[1] + blizzard_dy[ice_dir]*i] = 0
    # 1차원 맵 만들기
    one_dimension_Map = Make_one_dimension_Map(Map, one_dimension_Map_pos)
    # 맵 깨끗하게
    clean_Map() 
    # 맵 반영하기
    change_Map(one_dimension_Map_pos, one_dimension_Map)
    flag = True
    while flag:
        # 폭발 단계
        flag, one_dimension_Map = boom_Map(one_dimension_Map)
        # 맵 반영하기
        change_Map(one_dimension_Map_pos, one_dimension_Map)
        one_dimension_Map = Make_one_dimension_Map(Map, one_dimension_Map_pos)
        clean_Map() 
        change_Map(one_dimension_Map_pos, one_dimension_Map)
    # 구슬 변화 단계
    one_dimension_Map = Change_ball_by_one_dimension_Map(one_dimension_Map)
    clean_Map()
    change_Map(one_dimension_Map_pos, one_dimension_Map)
    
for i in range(1, 4):
    realanswer += i *answer[i]
print(realanswer)