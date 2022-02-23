def solution(record):
    answer = []
    database = dict()
    for ret in record:
        data = ret.split()
        # print(data)
        if data[0] == 'Enter':
            database[data[1]] = data[2] # uid
        elif data[0] == 'Change':
            database[data[1]] = data[2] # uid
    for ret in record:
        data = ret.split()
        if data[0] == 'Change':
            continue
        x = ""
        x += database[data[1]]
        x += "님이 "
        if data[0] == 'Enter':
            x += "들어왔습니다."
        elif data[0] == 'Leave':
            x += "나갔습니다."
        answer.append(x)
    return answer