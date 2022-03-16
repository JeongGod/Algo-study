class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        negative = []
        positive = []
        zero = False
        zerocnt = 0
        for num in nums:
            if(num < 0):
                negative.append(num)
            elif(num > 0):
                positive.append(num)
            else:
                zero = True
                zerocnt += 1
        # 음수 1개 양수 2개
        for negative_num in negative:
            left = 0
            right = len(positive)-1
            while left < right:
                if(positive[left] + positive[right] == -negative_num):
                    answer.append([negative_num, positive[left], positive[right]])
                    left += 1
                elif(positive[left] + positive[right] > -negative_num):
                    right -= 1
                else:
                    left += 1
        
        # 음수 2개 양수 1개
        for positive_num in positive:
            left = 0
            right = len(negative)-1
            while left < right:
                if(negative[left] + negative[right] == -positive_num):
                    answer.append([negative[left], negative[right], positive_num])
                    left += 1
                elif(negative[left] + negative[right] > -positive_num):
                    right -= 1
                else:
                    left += 1
        # 0 이 있을 때
        if(zero):
            if zerocnt >= 3:
                answer.append([0,0,0])
            negative = set(negative)
            positive = set(positive)
            for positive_num in positive:
                if(-positive_num in negative):
                    answer.append([-positive_num, 0, positive_num])
        
        answer = list(set([tuple(el) for el in answer]))
        return answer