def solution(n,a,b):
    answer = 0
    pivot = n/2
    turn = 0
    while True:
        if(n == 1):
            break
        n /= 2
        turn += 1
    answer = turn   
    nexthalf = pivot/2
    
    while True:
        if((a <= pivot and b > pivot) or (a > pivot and b <= pivot)):
            answer = turn
            break
        
        elif(a > pivot and b > pivot):
            pivot = pivot + nexthalf
        elif(a <= pivot and b <= pivot):
            pivot = pivot - nexthalf
        turn -= 1 
        nexthalf /=2
    return answer