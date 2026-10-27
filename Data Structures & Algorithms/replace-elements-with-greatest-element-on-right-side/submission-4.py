class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # if len(arr) == 1:
        #     arr[0] = -1

        # for i in range(len(arr)-1):
        #     right_win = arr[i + 1:]
        #     max_right_win = max(right_win)
        #     arr[i] = max_right_win
        #     if i == len(arr) - 2:
        #         arr[-1] = -1
        # return arr
        # Pattern used: suffix max, iterate backwards
        arr_len = len(arr)
        ans = [0] * arr_len
        right_max = -1
        for i in range(arr_len-1, -1, -1):
            ans[i] = right_max
            right_max = max(right_max, arr[i])
        return ans
        