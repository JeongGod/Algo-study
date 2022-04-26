word = ['A', 'E', 'I', 'O', 'U']
answer = 0

def dfs(cur, depth, target):
    global result, answer
    
    if cur == target:
        return True
    if depth == 5:
        return False
    
    for w in word:
        answer += 1
        result = dfs(cur + w, depth + 1, target)
        if result:
            return True
    
def solution(word):
    dfs("", 0, word)
    return answer