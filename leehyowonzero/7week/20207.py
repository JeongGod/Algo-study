n = int(input())
calendar = [0 for _ in range(366)]
for _ in range(n):
	start, end = map(int,input().split())
	for i in range(start, end+1):
		calendar[i] += 1
answer = 0
i = 1
while i < 366:
	if(calendar[i] != 0):
		max_row = 0
		col = 0
		while i < 366 and calendar[i] != 0:
			max_row = max(calendar[i], max_row)
			col += 1
			i += 1
		answer += max_row * col
	i += 1
print(answer)