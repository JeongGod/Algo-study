import sys

input = sys.stdin.readline
flag = False
def night(people, days, mafia):
    if flag:
        return
    # 죽인다.
    for person in range(N):
        if person == mafia or killed[person]:
            continue

        killed[person] = True
        for i in range(N):
            guilty[i] += change[person][i]
        day(people-1, days+1, mafia)
        for i in range(N):
            guilty[i] -= change[person][i]
        killed[person] = False

def day(people, days, mafia):
    global answer, flag

    if flag:
        return
    if people == 1:
        answer = max(answer, days)
        flag = True
        return
    # 유죄 지수가 가장 높은 사람을 죽인다.
    max_val = -1
    person = 0
    for idx in range(N):
        if killed[idx]:
            continue
        if guilty[idx] > max_val:
            person = idx
            max_val = guilty[idx]
    
    if person == mafia:
        answer = max(answer, days)
        return
    killed[person] = True
    night(people-1, days, mafia)
    killed[person] = False
    

if __name__ == "__main__":
    N = int(input())
    guilty = list(map(int, input().split()))
    killed = [False] * N
    change = []
    for _ in range(N):
        change.append(list(map(int, input().split())))
    
    mafia = int(input())

    answer = 0
    
    if N % 2 == 0:
        night(N, 0, mafia)
    else:
        day(N, 0, mafia)
    print(answer)
"""
16
100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100
1 4 3 -2 1 4 3 -2 1 4 3 -2 1 4 3 -2
-2 1 4 3 -2 1 4 3 -2 1 4 3 -2 1 4 3
3 -2 1 4 3 -2 1 4 3 -2 1 4 3 -2 1 4
4 3 -2 1 4 3 -2 1 4 3 -2 1 4 3 -2 1
1 4 3 -2 1 4 3 -2 1 4 3 -2 1 4 3 -2
-2 1 4 3 -2 1 4 3 -2 1 4 3 -2 1 4 3
3 -2 1 4 3 -2 1 4 3 -2 1 4 3 -2 1 4
4 3 -2 1 4 3 -2 1 4 3 -2 1 4 3 -2 1
1 4 3 -2 1 4 3 -2 1 4 3 -2 1 4 3 -2
-2 1 4 3 -2 1 4 3 -2 1 4 3 -2 1 4 3
3 -2 1 4 3 -2 1 4 3 -2 1 4 3 -2 1 4
4 3 -2 1 4 3 -2 1 4 3 -2 1 4 3 -2 1
1 4 3 -2 1 4 3 -2 1 4 3 -2 1 4 3 -2
-2 1 4 3 -2 1 4 3 -2 1 4 3 -2 1 4 3
3 -2 1 4 3 -2 1 4 3 -2 1 4 3 -2 1 4
4 3 -2 1 4 3 -2 1 4 3 -2 1 4 3 -2 1
1
"""
