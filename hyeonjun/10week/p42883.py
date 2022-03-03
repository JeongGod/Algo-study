def solution(number, k):
    answer = ''
    for idx, elm in enumerate(number):
        while answer and answer[-1] < elm and k:
            answer = answer[:-1]
            k -= 1
        answer += elm

        if not k:
            return answer + number[idx+1:]
    if k:
        return answer[:-k]
