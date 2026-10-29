class Solution:
    def isValid(self, s: str) -> bool:
        is_valid = False
        stack = []
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            elif stack:
                open_brac = stack[-1]
                if i == ')' and open_brac == '(':
                    stack.pop()
                elif i == ']' and open_brac ==  '[':
                    stack.pop()
                elif i == '}' and open_brac ==  '{':
                    stack.pop()
                is_valid = True
            else:
                stack.append(i)
        return is_valid and len(stack) == 0


        
        