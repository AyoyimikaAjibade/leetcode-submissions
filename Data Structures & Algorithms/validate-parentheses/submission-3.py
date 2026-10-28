class Solution:
    def isValid(self, s: str) -> bool:
        is_valid = False
        stack = []
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
                print('STACK OPEN', stack)
            elif stack:
                open_brac = stack[-1]
                if i == ')' and open_brac == '(':
                    stack.pop()
                    print('STACK CLOSE )', stack)
                elif i == ']' and open_brac ==  '[':
                    stack.pop()
                    print('STACK CLOSE ]', stack)
                elif i == '}' and open_brac ==  '{':
                    stack.pop()
                    print('STACK CLOSE }', stack)
                is_valid = True
            print('stack', stack, is_valid)
        return is_valid and len(stack) == 0


        