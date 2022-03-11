from collections import defaultdict

target_size = int(input())
m, n = map(int, input().split())
pizza_A = []
pizza_B = []
for _ in range(m):
    pizza_A.append(int(input()))
for _ in range(n):
    pizza_B.append(int(input()))

pizza_A_candi = [0, sum(pizza_A)]
for start_idx in range(m):
    candi = 0
    for i in range(0,m-1):
        candi += pizza_A[(start_idx + i)%m]
        pizza_A_candi.append(candi)
        
pizza_B_candi = [0, sum(pizza_B)]
for start_idx in range(n):
    candi = 0
    for i in range(0,n-1):
        candi += pizza_B[(start_idx + i)%n]
        pizza_B_candi.append(candi)

pizza_A_candi.sort()
pizza_B_candi.sort()
pizza_A_candi_dict = defaultdict(int)
pizza_B_candi_dict = defaultdict(int)

for candi in pizza_A_candi:
    pizza_A_candi_dict[candi] += 1
for candi in pizza_B_candi:
    pizza_B_candi_dict[candi] += 1
    
pizza_A_candi = list(set(pizza_A_candi))
pizza_B_candi = list(set(pizza_B_candi))
    
answer = 0
pizza_A_idx = 0 # 작은거부터
pizza_B_idx = len(pizza_B_candi) -1 # 큰거부터
while pizza_A_idx < len(pizza_A_candi) and 0 <= pizza_B_idx:
    candi = pizza_A_candi[pizza_A_idx] + pizza_B_candi[pizza_B_idx]
    if(candi == target_size):
        answer += pizza_A_candi_dict[pizza_A_candi[pizza_A_idx]] * pizza_B_candi_dict[pizza_B_candi[pizza_B_idx]]
        pizza_A_idx += 1
    elif(candi > target_size):
        pizza_B_idx -= 1
    else:
        pizza_A_idx += 1
        
print(answer)