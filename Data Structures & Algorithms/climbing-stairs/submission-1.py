class Solution:
    my_dict = {1:1,2:2}
    def climbStairs(self, n: int) -> int:
        # n(4) = n(3)+ n(2)
        if n in self.my_dict:
            return self.my_dict[n]
        else:
            self.my_dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.my_dict[n]

    

        