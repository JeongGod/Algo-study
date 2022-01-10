def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        temp = []
        flag = True
        for s in skill_tree:
            if s in skill:
                temp.append(s)
        for i in range(len(temp)):
            if temp[i] != skill[i]:
                flag = False
                break
        if flag:
            answer += 1
    return answer
