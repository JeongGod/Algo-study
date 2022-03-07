import sys

input = sys.stdin.readline

# RIGHT, UP, LEFT, DOWN 순
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def draw_curve(curve : list[int]) -> set[int]:
    sx, sy, d, age = curve

    visited = set()
    st = [d]
    visited.add((sx, sy))
    cx, cy = sx + dx[d], sy + dy[d]
    visited.add((cx, cy))
    # 세대만큼 반복
    for _ in range(age):
        # st에 들어있는 만큼 90도 회전
        for i in range(len(st)-1, -1, -1):
            d = st[i]
            nd = (d+1)%4
            cx, cy = cx + dx[nd], cy + dy[nd]
            visited.add((cx, cy))
            st.append(nd)

    return visited


if __name__ == "__main__":
    N = int(input())
    visited = set()
    for _ in range(N):
        curve = list(map(int, input().split()))
        visited |= draw_curve(curve)
    answer = 0
    for x in range(100):
        for y in range(100):
            if (x, y) in visited and\
                (x+1, y) in visited and\
                (x, y+1) in visited and\
                (x+1, y+1) in visited:

                answer += 1
    print(answer)
