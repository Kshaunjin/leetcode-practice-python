class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        total = []
        t2 = []
        for item in arr2:
            for i in arr1:
                if i == item:
                    total.append(i)
        
        for j in arr1:
            if j not in arr2:
                t2.append(j)
        t2.sort()
        #print(t2)
        total.extend(t2)
        #print(total)
        return total
