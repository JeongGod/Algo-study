from typing import List


def word_diff(a: str, b: str) -> int:
    diff: int = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
    return diff


def solution(begin: str, target: str, words: List[str]) -> int:
    answer: List[int] = []

    if target not in words:
        return 0

    for idx, word in enumerate(words):
        if word_diff(begin, word) <= 1:
            length: int = 0
            for next in words[idx:]:
                length += 1
                diff: int = word_diff(target, next)

                if diff == 0:
                    break

                if diff == 1:
                    length += 1
                    break

            answer.append(length)

    return min(answer)
