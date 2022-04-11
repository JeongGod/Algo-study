from itertools import permutations

def check_cost(sequence, cost):
    value = 0
    for selected_potion_idx in sequence:
        value += cost[selected_potion_idx]
        for discounted_potion in potion_discount[selected_potion_idx]:
            discounted_potion_idx, discounted_cost = discounted_potion
            cost[discounted_potion_idx] -= discounted_cost
            if(cost[discounted_potion_idx] <= 0):
                cost[discounted_potion_idx] = 1
    return value

n = int(input())
potion_cost = [0] + list(map(int,input().split()))
potion_discount = [[] for _ in range(n+1)]
for i in range(1, n+1):
    discount_num = int(input())
    for _ in range(discount_num):
        potion_discount[i].append(list(map(int,input().split()))) # [aj, dj]
potion = [i for i in range(1, n+1)]
save_potion_cost = potion_cost[:]
answer = 10001
for case in list(permutations(potion)):
    answer = min(answer, check_cost(case, potion_cost))
    potion_cost = save_potion_cost[:]
print(answer)
