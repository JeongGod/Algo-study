def solution(cookie):
    answer = 0
    for pivot in range(1,len(cookie)):
        left = 0
        right = len(cookie)-1
        leftsum = sum(cookie[left:pivot])
        rightsum = sum(cookie[pivot:right+1])
        while(left <= pivot and right >= pivot):
            if(leftsum == rightsum):
                answer = max(leftsum,answer)
                break
            elif(leftsum > rightsum):
                leftsum -= cookie[left]
                left += 1
            elif(leftsum < rightsum):
                rightsum -= cookie[right]
                right -= 1
    return answer