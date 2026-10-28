class Solution:
    def isValid(self, s: str) -> bool:
        is_valid = False
        stack = []
        for i in s:
            if i == '(' or '[' or '{':
                stack.append(i)
            else:
                if i == ')' and '(' in stack:
                    stack.pop()
                elif i == ']' and '[' in stack:
                    stack.pop()
                elif i == '}' and '{' in stack:
                    stack.pop()
                is_valid = True
            print('stack', stack)
        return is_valid and len(stack) == 0


        