from typing import Dict, List, Set, Tuple


def solution(id_list: List[str], report: List[str], k: int) -> List[int]:
    answer: List[int] = [0] * len(id_list)
    record: Set[Tuple[str, str]] = set()
    called_book: Dict[str, List[str]] = dict()  # 유저별 신고한 유저 모음

    for ids in report:
        caller, callee = ids.split(" ")
        record.add((caller, callee))

    for ids in record:
        caller, callee = ids

        if callee in called_book:
            called_book[callee].append(caller)
        else:
            called_book[callee] = [caller]

    for _, value in called_book.items():
        if len(value) >= k:
            for user in value:
                answer[id_list.index(user)] += 1

    return answer
