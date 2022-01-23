from collections import deque
from typing import Deque, List, Set, Tuple


def can_transform(source: str, target: str) -> bool:
    diff: int = 0
    for schar, tchar in zip(source, target):
        if schar != tchar:
            diff += 1
    return diff == 1


def solution(begin: str, target: str, words: List[str]) -> int:
    answer: int = 0
    que: Deque[Tuple[str, int, Set[str]]] = deque()

    que.append((begin, 0, set([begin])))

    while que:
        word, stage, visited = que.popleft()

        for cand in words:
            if cand in visited:
                continue
            if not can_transform(word, cand):
                continue

            if cand == target:
                return stage + 1

            que.append((cand, stage + 1, visited | set([cand])))

    return answer


# 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# 0
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
