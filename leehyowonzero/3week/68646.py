def solution(a):
    answer = 2
    if(len(a) <= 2):
        return len(a)
    leftmin = a[0]
    rightmin = min(a[1:])
    for i in range(1,len(a)-1):
        if(a[i] == rightmin):
            answer += 1
            leftmin = rightmin
            break
        else:
            if(a[i] > leftmin and a[i] > rightmin):
                continue
            else:
                answer += 1
                leftmin = min(leftmin, a[i])
    rightmin = a[-1]
    for j in range(len(a)-2, i, -1):
        if(a[j] > leftmin and a[j] > rightmin):
                continue
        else:
            answer += 1
            rightmin = min(rightmin, a[j])
    
    return answer