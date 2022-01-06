# 각 skill_trees의 빌드별로 스킬을 배운 시기를 저장하고, 선행스킬에 해당하는 스킬의 시기가 오름차순인지 확인하는 방식

def check(skill): # 스킬빌드가 적합한지 판단하는 함수
    global WhenUseSkill
    priorSkillArr = []
    
    for el in list(skill): # 선행스킬 순서대로 검사
        priorSkillArr.append(WhenUseSkill[ord(el) - 65])
    
    for i in range(len(priorSkillArr)-1): # 오름차순 검사
        if(priorSkillArr[i] > priorSkillArr[i+1]):
            return 0
    return 1
def solution(skill, skill_trees):
    answer = 0
    for case in skill_trees:
        global WhenUseSkill
        WhenUseSkill = [27 for _ in range(26)] # 어떤 알파벳의 스킬을 언제 사용하였는지 저장하는 배열 # 27로 초기화한 이유는 스킬 빌드가 적합한지 판단함에 있어 사용하기 위해 안배운 스킬의 경우 나올 수 없는 큰 수 27로 초기화
        for i, el in enumerate(case):
            WhenUseSkill[ord(el) - 65] = i # 아스키코드상 65 : 'A'
        answer += check(skill)
    return answer