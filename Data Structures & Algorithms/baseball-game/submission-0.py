class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for item in operations:
            if item != '+' and item != 'D' and item != 'C':
                stack.append(int(item))
            elif item == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2)
                stack.append(num1)
                stack.append(int(num1) + int(num2))
            elif item == 'D':
                num = stack.pop()
                stack.append(num)
                stack.append(2 * int(num))
            elif item == 'C':
                stack.pop()
        sum = 0
        for item in stack:
            sum += item
        return sum

        