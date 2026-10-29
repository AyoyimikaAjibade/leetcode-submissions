class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                if not stack:
                    return False
                open_brac = stack[-1]
                if (i == ')' and open_brac != '(') or \
                (i == ']' and open_brac !=  '[') or \
                (i == '}' and open_brac !=  '{'):
                    return False
                stack.pop()

        return len(stack) == 0


        