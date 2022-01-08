import sys
from typing import List, Set


IMP = sys.maxsize


def learn(skill: str, skill_tree: str) -> int:
    skills: Set[str] = set(list(skill_tree))

    learning_index: List[int] = [
        skill_tree.index(sk) if sk in skills else IMP for sk in skill
    ]

    for idx in range(1, len(learning_index)):
        prev, cur = learning_index[idx - 1], learning_index[idx]
        if prev > cur:
            return 0
    return 1


def solution(skill: str, skill_trees: List[str]):
    return sum(learn(skill, x) for x in skill_trees)


# 2
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
