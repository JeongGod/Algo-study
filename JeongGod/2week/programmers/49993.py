def solution(skill, skill_trees):
    _skill = {val : idx for idx, val in enumerate(skill)}
    answer = 0
    
    def check(s):
        learned_idx = 0
        for user_skill in s:
            # 현재 배운 스킬이 주어진 스킬트리에 존재하는지
            if user_skill not in _skill:
                continue
            # 해당 스킬이 주어진 스킬트리의 구조에 맞게 되고 있는지
            need_idx = _skill[user_skill]

            if learned_idx < need_idx:
                return False
            elif learned_idx == need_idx:
                learned_idx += 1
        return True
    for skill_tree in skill_trees:
        if check(skill_tree):
            answer += 1
    return answer