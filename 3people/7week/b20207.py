n = int(input())
cal = [0 for _ in range(366)]
for _ in range(n):
  a, b = map(int, input().split())
  for i in range(a, b+1):
    cal[i] += 1
answer = 0
row = 0
col = 0
for c in cal:
  if c == 0:
    answer += col * row
    col, row = 0, 0
  else:
    row = max(row, c)
    col += 1
answer += row * col
print(answer)