from itertools import combinations
# 유일성을 만족시키는 후보키 집합들을 찾기
# 그 후 최소성을 만족시키지 못하는 후보키 거르기
def CheckUniqueness(case, relation): # 유일성 체크
    candiset = set()
    for el in relation:
        candi = tuple([el[key] for key in case])
        if(candi not in candiset):
            candiset.add(candi)
        else:
            return False
    return True
        
def CheckMinimality(candi):
    ret = 0 
    for i in range(len(candi)):
        flag = True
        for j in range(len(candi)):
            if(i == j):
                continue
            if(set(candi[i]) & set(candi[j]) == set(candi[j])):
                flag = False
                break
        if(flag):
            ret += 1
    return ret
def solution(relation):
    candi = []
    row = len(relation)
    col = len(relation[0])
    attribute = [i for i in range(0,col)]
    # 모든 후보키 집합
    for i in range(1, col+1): # 고른 후보키의 길이
        for case in list(combinations(attribute, i)):
            if(CheckUniqueness(case, relation)):
                candi.append(case)
    # 최소성 체크
    answer = CheckMinimality(candi)
    return answer