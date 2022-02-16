from typing import List


def pick(board : List[List[int]], val : int) -> int:
    for i in range(len(board)):
        if board[i][val] != 0:
            result = board[i][val]
            board[i][val] = 0
            return result
    return 0

def solution(board, moves):
    answer = 0
    st = []

    for m in moves:
        result = pick(board, m-1)
        if result == 0:
            continue
        if st and st[-1] == result:
            st.pop()
            answer += 2
        else:
            st.append(result)
    
    return answer
