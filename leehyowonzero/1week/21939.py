import heapq
import sys
input = sys.stdin.readline

n = int(input())
maxq = []
minq = []
visited = [0 for _ in range(10**5 + 1)]
for _ in range(n):
	p, l = map(int,input().split())
	visited[p] = l
	maxq.append((-l,-p))
	minq.append((l,p))
heapq.heapify(maxq)
heapq.heapify(minq)

m = int(input())
for _ in range(m):
	command = input().split()
	if(command[0] == 'recommend'):
		if(command[1] == '1'):
			while(visited[-maxq[0][1]] == 0 or visited[-maxq[0][1]] != -maxq[0][0]):
				heapq.heappop(maxq)	
			l, p = maxq[0]
			print(-p)
		else:
			while(visited[minq[0][1]] == 0 or visited[minq[0][1]] != minq[0][0]):
				heapq.heappop(minq)	
			l, p = minq[0]
			print(p)
	elif(command[0] == 'add'):
		command[1] = int(command[1])
		command[2] = int(command[2])
		heapq.heappush(maxq,(-command[2], -command[1]))
		heapq.heappush(minq,(command[2], command[1]))
		visited[command[1]] = command[2]
	elif(command[0] == 'solved'):
		command[1] = int(command[1])
		visited[command[1]] = 0
