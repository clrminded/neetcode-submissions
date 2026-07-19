class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity > 0:
            self.capacity = capacity
            self.A = []
        
    def get(self, i: int) -> int:
        return self.A[i]

    def set(self, i: int, n: int) -> None:
        self.A[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.A.append(n)
        

    def popback(self) -> int:
        return self.A.pop()
 

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:
        return len(self.A)
        
    
    def getCapacity(self) -> int:
        return self.capacity