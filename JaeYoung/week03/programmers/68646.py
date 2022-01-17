def solution(a):
    check = [False] * len(a) 
    start = 10 ** 10
    end = 10 ** 10

    for i in range(len(a)): #왼쪽에서부터 체크
        if a[i] < start:
            start = a[i]
            check[i] = True
        
    for i in range(len(a)): #오른쪽에서부터 다시 체크
        if a[-i - 1] < end:
            end = a[-i - 1]
            check[-i - 1] = True
    
    
    return sum(check)