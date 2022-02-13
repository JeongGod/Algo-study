from collections import deque

n = int(input())
answer = [float('inf'),0]

q = deque()
q.append([str(n), 0]) # 값, 점수
while q :
    string, value = q.popleft()

    for el in string:
        if(int(el)%2 == 1): # 각 자리수가 홀수인지 확인
            value += 1
			
    if(len(string) == 1): # 수가 한자리이면
        answer[0] = min(answer[0], value)
        answer[1] = max(answer[1], value)
        continue
		
    elif(len(string) == 2): # 수가 두자리이면
        q.append([str(eval(string[0] + '+' + string[1])), value])
		
    else: # 수가 세자리 이상이면
        for i in range(1, len(string)-1): # 임의의 위치로 자름
            for j in range(i+1,len(string)):
                q.append([str(eval(string[0:i] + '+' + str(int(string[i:j])) + '+' + str(int(string[j:])))), value])
print(*answer)	