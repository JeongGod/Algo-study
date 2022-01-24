import copy

def ispossible(start, destination):
    if(start == destination[0]):
        return True
    return False

def dfs(start, leasttickets, ans ,cnt):
    global answer
    global n
    if cnt == n and answer == []:
        answer = ans[:]
        return
    
    for i in range(len(leasttickets)):
        beforticket = copy.deepcopy(leasttickets)
        if(ispossible(start, leasttickets[i])):
            chosse = beforticket[i][1]
            ans.append(chosse)
            beforticket.pop(i)
            dfs(chosse,beforticket,ans,cnt+1 )
            ans.pop(-1)
            
def solution(tickets):
    global answer
    global n
    answer = []
    start = "ICN"
    n = len(tickets)
    tickets.sort(key = lambda x : x[1]) # 알파벳 순서가 앞서는 경로 순으로 탐색하기 위해
    dfs(start, tickets, ["ICN"], 0)
    return answer