def solution(gems):
    TYPE_NUM = len(set(gems)) # 종류개수
    GEM_NUM = len(gems) # 진열대 길이
    answer = []
    start, end = 0, 0
    DIST, INDEX = 0, 1 # 구간, index
    # 초기값
    cur_shop = {gems[0]: 1}
    while start < GEM_NUM and end < GEM_NUM:
        if len(cur_shop) < TYPE_NUM: # 아직 전체 모음 아님
            end += 1
            if end == GEM_NUM:
                break
            cur_shop[gems[end]] = cur_shop.get(gems[end], 0) + 1
        else:
            answer.append((end-start, [start+1, end+1]))
            cur_shop[gems[start]] -= 1
            if cur_shop[gems[start]] == 0:
                del cur_shop[gems[start]]
            start += 1
    answer = sorted(answer, key=lambda x: (x[DIST], x[INDEX]))
    return answer[0][INDEX]