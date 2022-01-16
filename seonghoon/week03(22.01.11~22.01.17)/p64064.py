from itertools import product
from typing import FrozenSet, List, Set, Tuple


def ismatched(user: str, banned: str) -> bool:
    if len(user) != len(banned):
        return False

    for uchar, bchar in zip(user, banned):
        if uchar != bchar and bchar != "*":
            return False
    return True


def solution(user_id: List[str], banned_id: List[str]) -> int:
    matched_ids: List[List[str]] = [
        [user for user in user_id if ismatched(user, banned)] for banned in banned_id
    ]

    length: int = len(banned_id)
    candidates: Set[FrozenSet[Tuple[str, ...]]] = set(
        [frozenset(cand) for cand in product(*matched_ids) if len(set(cand)) == length]
    )
    return len(candidates)


# 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# 2
print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
    )
)
# 3
print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "*rodo", "******", "******"],
    )
)
# 1
print(
    solution(
        [
            "abcdefgh",
            "bcdefgha",
            "cdefghab",
            "defghabc",
            "efghabcd",
            "fghabcde",
            "ghabcdef",
            "habcdefg",
        ],
        [
            "********",
            "********",
            "********",
            "********",
            "********",
            "********",
            "********",
            "********",
        ],
    )
)
