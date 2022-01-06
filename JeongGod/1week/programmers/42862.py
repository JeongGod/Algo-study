def solution(n, lost, reserve):
    """
    1. 잃어버린 학생부터 그 앞의 학생한테 빌려본다.
    2. 빌리지 못 했다면 그 뒤의 학생에게 빌린다.
    """
    # 여분이 있는 애들 중 빼앗기지 않은 애들
    reserve, lost = set(reserve) - set(lost), set(lost) - set(reserve)
    # 전체 학생에서 일단 가능한 학생들의 수
    answer = n - len(lost)
    for student in lost:
        # 잃어버린 학생 중 빌릴 수 있는지 체크
        if student - 1 in reserve:
            answer += 1
        elif student + 1 in reserve:
            answer += 1
            reserve.remove(student+1)
    
    return answer
