from collections import deque


def solution(priorities, location):
    """
    중요도를 갖고 있는 배열이 존재해야한다.
    정렬해서 가자.
    """
    order = sorted(priorities, reverse=True)
    target_idx = 0
    dq = deque(list(enumerate(priorities)))
    while dq:
        idx, val = dq.popleft()
        # 뽑는다.
        if val == order[target_idx]:
            target_idx += 1
            if idx == location:
                return target_idx
            continue
        # 뒤로 보낸다.
        dq.append((idx, val))
