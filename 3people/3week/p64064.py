from itertools import permutations

def check_ban(user, ban):
    for i in range(len(ban)):
        if len(user[i]) != len(ban[i]):
            return False
        for j in range(len(user[i])):
            if ban[i][j] == '*':
                continue
            if ban[i][j] != user[i][j]:
                return False
    return True
                
def solution(user_id, banned_id):
    s = []
    user_permutation = list(permutations(user_id, len(banned_id)))
    for user in user_permutation:
        if check_ban(user, banned_id):
            user = set(user)
            if user not in s:
                s.append(user)
    return len(s)