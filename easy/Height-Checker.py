class Solution:
    def heightChecker(self, heights: List[int]) -> int:
	#heights:[1,1,4,2,1,3]
        #print(heights)
        #a = set(heights)
        a = heights.copy()
        heights.sort()
        b = heights
        #b = set(heights)
        print(a,b)
        count = 0
        for i,item in enumerate(a):
            if item != b[i]:
                count+=1
        return count
