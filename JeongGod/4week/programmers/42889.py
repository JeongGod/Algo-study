from collections import Counter


def solution(N, stages):
    """
    (i)번째 stage에 머물러있는 사람 / len(stages)
    len(stages) -= (i)번째 stage에 머물러있는 사람
    """
    by_stage = Counter(stages)
    people = len(stages)
    answer = []
    for stage in range(1, N+1):
        challengers = by_stage.get(stage)
        if challengers is None:
            answer.append((stage, 0))
            continue
        answer.append((stage, challengers/people))
        people -= challengers

    return list(map(lambda x:x[0], sorted(answer, key=lambda x:x[1], reverse=True)))
