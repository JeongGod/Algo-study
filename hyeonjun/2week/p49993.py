import re


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        simplified_skill = re.sub("[^" + skill + "]", "", skill_tree)
        if simplified_skill == skill[: len(simplified_skill)]:
            answer += 1
    return answer
