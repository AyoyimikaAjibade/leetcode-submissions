class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """start from 0 to length of arr
        move to ith value if ith value is 1
            1. keep track of 1 counts 
            2. keep track of the max

        if ith value not 1
            1. clear curr 1 counts 
            2. move starting value to next and repeat above step
        """
        curr_ones_total = 0
        max_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_ones_total += 1
            print('curr_ones_total', curr_ones_total)    
            max_ones = max(curr_ones_total, max_ones) 
            print('max_ones', max_ones)
            if nums[i] == 0:
                curr_ones_total = 0
                i += 1


        return max_ones
        