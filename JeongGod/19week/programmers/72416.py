import sys


def dfs(parent, cur, sales):
    global tree, dp
    
    # 트리의 끝이라면
    if not tree[cur]:
        dp[cur][0] = 0
        dp[cur][1] = sales[cur-1]
        return
    dp[cur][1] = sales[cur-1]
    
    # 자식을 탐색한다.
    for ncur in tree[cur]:        
        dfs(cur, ncur, sales)
        # 팀장 참가
        dp[cur][1] += min(dp[ncur])
    
    # 팀장이 참가하지 않는 경우
    tmp = 0
    flag = False
    min_diff = sys.maxsize
    for ncur in tree[cur]:
        # 현재 나를 품어줄 수 있는 친구라면
        if dp[ncur][1] <= dp[ncur][0]:
            flag = True
            tmp += dp[ncur][1]
        else:
            tmp += dp[ncur][0]
            # 차이가 적은 친구를 기억해둔다.
            if min_diff > dp[ncur][1] - dp[ncur][0]:
                min_diff = dp[ncur][1] - dp[ncur][0]
                min_idx = ncur
            
    if flag:
        dp[cur][0] = tmp
    else:
        dp[cur][0] = tmp - dp[min_idx][0] + dp[min_idx][1]
    
def solution(sales, links):
    global tree, dp
    
    answer = 0
    tree = [[] for _ in range(len(sales)+1)]
    dp = [[sys.maxsize, sys.maxsize] for _ in range(len(sales)+1)]
    
    for a, b in links:
        tree[a].append(b)
    
    dfs(0, 1, sales)

    return min(dp[1])
