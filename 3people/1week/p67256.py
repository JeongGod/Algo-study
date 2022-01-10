def solution(numbers, hand):
  answer = ''
  lhand = 10
  rhand = 12
  for number in numbers:
    if number in [1, 4, 7]:
      answer += 'L'
      lhand = number
    elif number in [3, 6, 9]:
      answer += 'R'
      rhand = number
    else:
      if number == 0:
        number = 11
      ldis = sum(divmod(abs(number - lhand), 3))
      rdis = sum(divmod(abs(number - rhand), 3))
      if ldis < rdis:
        answer += 'L'
        lhand = number
      elif ldis > rdis:
        answer += 'R'
        rhand = number
      else:
        if hand == 'left':
            answer += 'L'
            lhand = number
        elif hand == 'right':
            answer += 'R'
            rhand = number 
  return answer