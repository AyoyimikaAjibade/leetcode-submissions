class Solution:
    def isPalindrome(self, s: str) -> bool:
        # str = case insensitive ignore alpha numeric and spacing
        # words with spaces
   
        # remove space and convert to lower and ignore alpha numeric chars
        lower_s = s.lower()
        clean_s = ''
        for char in lower_s:
            if char.isalnum(): 
                clean_s += char

        left = 0
        right = len(clean_s) -1 
        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        return True



        # s = "Was it a car or a cat I saw?"
        