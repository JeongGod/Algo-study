
def check(user, ban):
    for k in range(len(user)):
        if ban[k] == "*":
            continue
        else:
            if(ban[k] != user[k]):
                return 0
    return 1

def solution(user_id, banned_id):
    bancaseByid = [ [] for _ in range(len(banned_id))]
    for i, ban in enumerate(banned_id):
        for j, user in enumerate(user_id):
            if(len(user) == len(ban) and check(user,ban)):    
                bancaseByid[i].append(str(j))
    answercase = ['']
    for banned_user in bancaseByid:
        nextanswercase = []
        for user in banned_user:
            for el in answercase:
                if(user not in el):
                    nextanswercase.append("".join([user,el]))
        answercase = nextanswercase
    for i in range(len(nextanswercase)):
        nextanswercase[i] = "".join(sorted(nextanswercase[i]))
    answercase = list(set(answercase))
    return len(answercase)
        