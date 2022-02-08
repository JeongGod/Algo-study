import sys

N = int(sys.stdin.readline())
schedule = [0 for _ in range(367)]
for _ in range(N):
    # 시작과 끝을 기록한다.
    start, end = map(int, sys.stdin.readline().split())
    schedule[start] += 1
    schedule[end + 1] -= 1

# 해당 일수마다 겹치는 개수를 센다.
for i in range(1, len(schedule)):
    schedule[i] += schedule[i - 1]

width, height, result = 0, 0, 0
for s in schedule:
    # 겹치는게 없을 때 계산한다.
    if s == 0:
        result += (width * height)
        width, height = 0, 0
    # 겹친다면 width를 늘리면서 제일 많이 겹치는 것을 기록한다.
    else:
        width += 1
        height = max(height, s)

print(result)
