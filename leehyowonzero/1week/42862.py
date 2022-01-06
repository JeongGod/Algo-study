def solution(n, lost, reserve):
    answer = 0
    haveclothes = [1 for _ in range(n+2)]
    haveclothes[0] = 0
    for el in lost:
        haveclothes[el] -= 1
    for el in reserve:
        haveclothes[el] += 1
    for i in range(1, n+1):
        if(haveclothes[i] == 1 or haveclothes[i] == 2):
            answer += 1
            haveclothes[i] -= 1
        elif(haveclothes[i] == 0):
            if(haveclothes[i-1] == 1):
                haveclothes[i-1] -= 1
                answer += 1
            elif(haveclothes[i+1] == 2):
                haveclothes[i+1] -=1
                answer += 1
    return answer