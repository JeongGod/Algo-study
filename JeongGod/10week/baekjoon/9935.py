import sys

input = sys.stdin.readline
"""
stack을 이용해서 폭발이 일어나게 한다.
"""

def solution(check_str : str, bomb : list[str]) -> str:
    st = []
    bomb_idx = 0
    """
    1. bomb[0] 부터 살펴보면서 같으면 증가한다. 다르다면 0으로 다시 초기화한다.
    2. 증가하다가 bomb의 길이와 같아지면 bomb의 길이만큼 pop한다.
    3. 반복한다.
    """
    for val in check_str:
        if val != bomb[bomb_idx]:
            bomb_idx = 0
        if val == bomb[bomb_idx]:
            bomb_idx += 1

        st.append((val, bomb_idx))
        
        if bomb_idx == len(bomb):
            for _ in range(bomb_idx):
                st.pop()
            bomb_idx = st[-1][1] if st else 0
        
    
    return "".join([val for val, _ in st]) if st else "FRULA"

if __name__ == "__main__":
    check_str = input().rstrip()
    bomb = input().rstrip()
    print(solution(check_str, list(bomb)))
