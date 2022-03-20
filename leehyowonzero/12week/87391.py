dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]

def solution(n, m, x, y, queries):
    answer = -1
    lower_x, upper_x = x, x
    lower_y, upper_y = y, y
    # 지금 x, y 에 모든 경우의수가 다 몰려있음 최종적으로
    # 이걸 query를 역으로 읽어가면서 쭉 펼쳐준다는 느낌 (유망한 놈들을 거를거다.)
    # 이때 유망한놈이 없는 순간이 찰나라도 생기면 return 0
    # 유망한놈의 수 : 위 lower upper 사각형의 넓이
    # 이 사각형을 확장시키는 과정에서 벽으로 막혀있는경우랑 안막혀있는 경우를 걸러야함
    # 윗무빙을 칠건데 위에가 막혀있으면 유망한 놈들의 범위가 그만큼 확장되지만,
    # 만약 막혀있지 않은 상태면 사각형의 모양은 변하지 않고 밑으로 당겨진다.
    for query in reversed(queries):
        d, dx = query
        if(d == 0): # 열번호가 감소하는 방향으로 이동하는 명령이므로 현재 유망한 사각형이 0번 열에 존재하는지가 중요함, 0번열이면 범위를 확장하고 아닐 시 좌표만 당김
            if(lower_y == 0):
                upper_y -= dxy[d][1] * dx
            else:
                lower_y -= dxy[d][1] * dx
                upper_y -= dxy[d][1] * dx
            if(upper_y >= m):
                upper_y = m-1
                
        if(d == 1): # 열번호가 증가하는 방향으로 이동하는 명령이므로 현재 유망한 사각형이 n-1번 열에 존재하는지가 중요함, 0번열이면 범위를 확장하고 아닐 시 좌표만 당김
            if(upper_y == m-1):
                lower_y -= dxy[d][1] * dx
            else:
                lower_y -= dxy[d][1] * dx
                upper_y -= dxy[d][1] * dx
            if(lower_y < 0):
                lower_y = 0
        if(d == 2): # 행번호가 감소하는 방향으로 이동하는 명령이므로 현재 유망한 사각형이 0번 행에 존재하는지가 중요함, 0번행이면 범위를 확장하고 아닐 시 좌표만 당김
            if(lower_x == 0):
                upper_x -= dxy[d][0] * dx
            else:
                lower_x -= dxy[d][0] * dx
                upper_x -= dxy[d][0] * dx
            if(upper_x >= n):
                upper_x = n-1
        if(d == 3): # 행번호가 증가하는 방향으로 이동하는 명령이므로 현재 유망한 사각형이 m-1번 행에 존재하는지가 중요함, 0번열이면 범위를 확장하고 아닐 시 좌표만 당김
            if(upper_x == n-1):
                lower_x -= dxy[d][0] * dx
            else:
                lower_x -= dxy[d][0] * dx
                upper_x -= dxy[d][0] * dx
            if(lower_x < 0):
                lower_x = 0
        
        # print(lower_x, upper_x, lower_y, upper_y)
        tmp = (upper_x - lower_x +1) * (upper_y - lower_y + 1)
        # print(tmp)
        if(tmp < 0):
            return 0
        
    return tmp