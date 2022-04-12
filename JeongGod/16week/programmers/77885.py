def find_zero_bit(n):
    idx = 0
    while n > 0:
        if n&1 == 0:
            break
        n >>= 1
        idx += 1
    return idx
def solution(numbers):
    """
    1. n보다 커야한다.
    2.  비트가 꽉 차있다면 -> 차상위 + 1, 차상위 반전
        중간에 0이 있다면 -> 해당 비트, 해당 비트 - 1 반전
        0이 마지막이라면 -> 해당 비트만 반전
    """
    answer = []
    for n in map(int, numbers):
        if n & 1 == 0:
            result = n | 1
            answer.append(result)
            continue
        zero = find_zero_bit(n)
        result = (n | (1 << zero)) ^ (1 << (zero-1))
        
        answer.append(result)
    
    
    return answer
