def solution(record):
    answer = []
    """
    Enter
        id : nickname
        id님이 들어왔습니다.
    Change
        id : nickname 변경
    Leave
        id님이 나갔습니다
    
    후에 answer배열에서 id를 nickname으로 변경
    """
    user = dict()
    for val in record:
        com, uid, *nickname = val.split()
        if com == "Enter":
            user[uid] = nickname[0]
            answer.append([uid, "님이 들어왔습니다."])
        elif com == "Change":
            user[uid] = nickname[0]
        elif com == "Leave":
            answer.append([uid, "님이 나갔습니다."])
    # uid => nickname으로 변경
    for idx in range(len(answer)):
        uid, word = answer[idx]
        answer[idx] = user[uid] + word
    
    
    return answer
