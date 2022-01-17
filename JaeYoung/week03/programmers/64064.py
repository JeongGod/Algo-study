from itertools import permutations
from typing import List
import re


def solution(user_id: List[str], banned_id: List[str]):

    # 제재 아이디 수만큼 모든 유저 아이디 순열 생성
    users_combi: List[List[str]] = list(
        map(list, permutations(user_id, len(banned_id))))
    answer: List[List[str]] = []

    for users in users_combi:
        ban_info: List[str] = banned_id[:]
        ban_users: List[str] = []

        for user in users:
            for ban_user in ban_info[:]:
                if len(user) != len(ban_user):
                    continue

                # 제재 아이디의 별(*) 문자를 정규표현식 문자로 바꿈
                p = re.compile(ban_user.replace("*", "[a-z0-9]"))
                if p.match(user):  # 유저 아이디가 제재 아이디 형식이랑 일치하면 ban_users 목록에 추가
                    ban_users.append(user)
                    del ban_info[ban_info.index(ban_user)]
                    break

        if len(ban_users) == len(banned_id):
            # answer 내 중복된 제재 아이디 목록 제거를 위해 정렬해서 추가
            answer.append(sorted(ban_users))

    # 중복된 제재 아이디 목록 제거 후 개수 반환
    return len(list(set(map(tuple, answer))))