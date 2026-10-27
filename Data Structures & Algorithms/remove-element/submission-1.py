class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """if nums ith values is same as val
        1. update value to 0 by removing(creating empty space)
        2. move next value back to that value index(means prev)   and shift other value
        3. else if ith values not same as val move to the next"""
        i = 0
        nums_len = len(nums)
        while i < nums_len:
            if nums[i] == val:
                nums_len -= 1
                nums[i] = nums[nums_len]
            else:
                i += 1
        return nums_len



    