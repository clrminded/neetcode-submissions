class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = 0

        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.curr_min = val
        elif val < self.curr_min:
            self.curr_min = val
        self.stack.append(val)
        

    def pop(self) -> None:
        if len(self.stack) <= 0:
            return
        self.stack.pop()
        # if current min was popped we got to account for it
        if len(self.stack) == 0:
            return
        self.curr_min = self.stack[0]
        for i in range(len(self.stack)):
            if self.stack[i] < self.curr_min:
                self.curr_min = self.stack[i]

        

    def top(self) -> int:
        last = len(self.stack) - 1
        return self.stack[last]
        

    def getMin(self) -> int:
        return self.curr_min

        
