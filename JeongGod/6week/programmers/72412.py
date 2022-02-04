from collections import defaultdict


def solution(info, query):
    """
    java, python, cpp, - => 4가지
    backend, frontend, - => 3가지
    junior, senior, - => 3가지
    pizza, chicken, - => 3가지
    
    (선택, -) 2가지 => 8가지
    
    5만 * 8 = 40만
    info -> query에 맞는 친구를 찾아준다.
    O(50만)
    """
    answer = []
    def dfs(user_info):
        result = []
        def per(idx, val):
            if idx == 4:
                result.append(val)
                return
            for i in [user_info[idx], "-"]:
                per(idx+1, val+i)
        per(0, "")
        return result
    
    query_dict = defaultdict(list)
    for user_info in map(lambda x:x.split(), info):
        for val in dfs(user_info):
            query_dict[val].append(int(user_info[-1]))
    
    # 정렬
    for key in query_dict:
        query_dict[key].sort()
    
    for q in query:
        infos, score = q.replace(" and ", "").split()
        score = int(score)
        cnt = 0
        left, right = 0, len(query_dict[infos])-1
        # 이분탐색
        while left <= right:
            mid = (left + right) // 2
            if query_dict[infos][mid] >= score:
                right = mid - 1
            else:
                left = mid + 1
        
        answer.append(len(query_dict[infos]) - left)

    return answer
