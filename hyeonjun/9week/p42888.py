def solution(record):
    answer = []
    uuid = {}

    for message in record:
        if message[0] == 'C' or message[0] == 'E':
            a, b, c = message.split()
            uuid[b] = c

    for message in record:
        if message[0] == 'E':
            a, b, c = message.split()
            answer.append(uuid[b] + '님이 들어왔습니다.')

        elif message[0] == 'L':
            a, b = message.split()
            answer.append(uuid[b] + '님이 나갔습니다.')

    return answer
