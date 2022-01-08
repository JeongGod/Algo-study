from typing import List


def solution(strings: List[str], n: int) -> List[str]:
    return sorted(strings, key=lambda x: (x[n], x))
