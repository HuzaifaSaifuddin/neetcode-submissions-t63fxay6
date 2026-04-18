class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxVal = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                maxVal = max(current,maxVal)
            else:
                current = 0
        
        return maxVal
