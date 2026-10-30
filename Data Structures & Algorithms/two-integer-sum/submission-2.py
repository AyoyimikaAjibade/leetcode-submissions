class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history_map = {}
        past_diff = 0
        for i in range(len(nums)):
            past_diff = target - nums[i]
            if past_diff in history_map:
                return [history_map[past_diff], i]
            history_map[nums[i]] = i