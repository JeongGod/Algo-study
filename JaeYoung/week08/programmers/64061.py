def pick_up(move) -> None:
    global answer, gboard, basket

    for col in range(len(gboard)):
        if col != move-1:
            continue
        for row in range(len(gboard)):
            kan = gboard[row][col]
                
            if kan == 0:
                continue
            if basket and basket[-1] == kan:
                basket.pop()
                gboard[row][col] = 0
                answer += 2
                break
            
            basket.append(kan)
            gboard[row][col] = 0
            break

def solution(board, moves):
    global answer, gboard, basket
    gboard = board[:]
    basket = []
    answer = 0
    
    for move in moves:
        pick_up(move)
    
    return answer