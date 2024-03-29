class Solution:
    def fib(self, N: int) -> int:
        if N == 0 or N == 1:
            return N
        a,b = 0,1
        for i in range(2,N+1):
            temp = b
            b = a+b
            a = temp
        return b
