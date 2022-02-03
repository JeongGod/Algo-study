def solution(id_list, report, k):
  id_reported = {id: [] for id in id_list}
  id_blocked = {id: 0 for id in id_list}
  ans = {id: 0 for id in id_list}
  s = set()
  
  for r in report:
    info = r.split()
    info_tuple = (info[0], info[1])
    s.add(info_tuple)
    if info[1] not in id_reported[info[0]]:
      id_reported[info[0]].append(info[1])
  for el in s:
    id_blocked[el[1]] += 1
  for key, value in id_blocked.items():
    if value >= k:
      for el in id_reported.items():
        if key in el[1]:
          ans[el[0]] += 1   
  answer = [value for _, value in ans.items()]
  return answer