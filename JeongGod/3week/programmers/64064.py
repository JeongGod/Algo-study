import re
from itertools import permutations
def solution(user_id, banned_id):
    answer = set()
    
    def check(per):
        # 해당 경우의 수가 가능한지 체크
        idx = 0
        for _, user in per:
            ban = banned_id[idx].replace("*", ".")
            pattern = re.compile(f"^{ban}$")

            if re.match(pattern, user) is None:
                return False
            else:
                idx += 1
        return True
    
    
    for per in permutations(enumerate(user_id), len(banned_id)):
        if check(per):
            answer.add(tuple(sorted(map(lambda x: x[0], per))))
            
                
    return len(answer)