class Solution:
    def isValid(self, s: str) -> bool:
        closing = [')', '}', ']']
        stack = []
        idx = 0
        while idx < len(s):
            if s[idx] not in closing:
                stack.append(s[idx])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top == '(' and s[idx] != closing[0]:
                    return False 
                elif top == '{' and s[idx] != closing[1]:
                    return False
                elif top == '[' and s[idx] != closing[2]:
                    return False
            idx += 1
        return True if not stack else False