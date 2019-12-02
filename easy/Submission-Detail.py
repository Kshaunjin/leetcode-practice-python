class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        for i in range(len(stones)):
            if len(stones)>1:
                last = stones[-1]
                before = stones[-2]
                stones = stones[0:len(stones)-2]
                left = abs(last-before)
                stones.append(left)
                stones.sort()
            #print(stones)
            
        #print(stones)
        #print(max(stones))
        return max(stones)
