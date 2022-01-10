def solution(skill, skill_trees):
    
    answer = len(skill_trees)
    
    for tree in skill_trees:
        tmp_skill = skill
        for x in tree:
            if x in tmp_skill: #배울 스킬이 선행스킬에 있고
                if tmp_skill[0] == x: #선행으로 배워야할 스킬이면 tmp_skill 의 해당 스킬을 삭제
                    tmp_skill = tmp_skill.replace(x, "")
                else: #선행으로 배워야할 스킬이 아니면 answer에 -1 해준다
                    answer -= 1
                    break

    return answer