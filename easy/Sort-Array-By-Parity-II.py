class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        B = []
        C = []
        D = []
        for item in A:
            if item % 2 == 0:
                C.append(item)
            else:
                B.append(item)
        
        half = len(A)//2
        for i in range(half):
            D.append(C[i])
            D.append(B[i])
        #print(D)
        return D
