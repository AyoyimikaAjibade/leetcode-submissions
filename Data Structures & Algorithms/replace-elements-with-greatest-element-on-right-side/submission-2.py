class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            arr[0] = -1

        for i in range(len(arr)-1):
            right_win = arr[i + 1:]
            max_right_win = max(right_win)
            arr[i] = max_right_win
            if i == len(arr) - 2:
                arr[-1] = -1
        return arr
        