def solution(record):
  answer = []
  actions = []
  dic = {}
  for r in record:
    temp = r.split()
    action, uid = temp[0], temp[1]
    if action == 'Enter' or action == 'Change':
      dic[uid] = temp[2]
    actions.append([action, uid])
  for action, uid in actions:
    if action == 'Enter':
      answer.append(f'{dic[uid]}님이 들어왔습니다.')
    elif action == 'Leave':
      answer.append(f'{dic[uid]}님이 나갔습니다.')
  return answer