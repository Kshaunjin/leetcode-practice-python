class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        #print(map(list,zip(*A)))
        
        return map(list,zip(*A))
