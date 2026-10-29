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
                    is_valid = True
                    print('STACK CLOSE )', stack)
                elif i == ']' and open_brac ==  '[':
                    stack.pop()
                    is_valid = True
                    print('STACK CLOSE ]', stack)
                elif i == '}' and open_brac ==  '{':
                    stack.pop()
                    is_valid = True
                    print('STACK CLOSE }', stack)
            else:
                stack.append(i)
            print('stack', stack, is_valid)
        return is_valid and len(stack) == 0


        