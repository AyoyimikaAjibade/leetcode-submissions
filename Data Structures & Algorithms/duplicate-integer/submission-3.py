class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for num in nums:
            if not num in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
                
            if nums_map[num] > 1:
                return True
        return False
            
        