answer = 0
def solution(cookie):
    """
    m번째를 고른다.
    m-1, m+1 투포인터를 이용하여 하나씩 증가한다.
    1. 왼쪽의 합 < 오른쪽의 합
        왼쪽을 하나씩 늘린다.
    2. 왼쪽의 합 > 오른쪽의 합
        오른쪽을 하나씩 늘린다.
    3. 왼쪽의 합 == 오른쪽의 합
        answer에 큰 값을 넣는다.
    """
    def two_pointer(m):
        global answer
        left = m
        right = m+1
        left_sum, right_sum = cookie[left], cookie[right]
        while True:
            if left_sum < right_sum:
                left -= 1
                if left < 0:
                    break
                left_sum += cookie[left]
            elif left_sum > right_sum:
                right += 1
                if right >= len(cookie):
                    break
                right_sum += cookie[right]
            else:
                if left_sum > answer:
                    answer = left_sum
                left -= 1
                if left < 0:
                    break
                left_sum += cookie[left]

    # 맨 오른쪽을 가졌을 때는 왼쪽 오른쪽을 나눌 수 없다.
    for m in range(len(cookie)-1):
        two_pointer(m)
    return answer