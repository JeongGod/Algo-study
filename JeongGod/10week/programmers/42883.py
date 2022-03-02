def solution(number, k):
    """
    내림차순으로 가면 최댓값이 나온다.
    1. n[-1] >= val
        일단 더한다.
    2. n[-1] < val
        n[-1]은 버리고
        1이 나올때 까지 계속 반복한다.
        그 다음에 val을 추가한다.
    """
    n = [number[0]]
    for val in number[1:]:
        while n and k > 0 and n[-1] < val:
            n.pop()
            k -= 1
        n.append(val)
    answer = "".join(n[:len(number)-k])
    
    return answer
