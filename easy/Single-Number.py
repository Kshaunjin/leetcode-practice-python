class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #print(nums)
        dict = {}
        for item in nums:
            item = str(item)
            #print(item)
            if item in dict:
                #print(item)
                dict[item]+=1
            else:
                dict[item] = 1
        #print(dict)
        return min(dict, key=dict.get)
