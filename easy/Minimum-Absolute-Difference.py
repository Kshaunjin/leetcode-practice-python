class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        num = 0
        c = []
        for i in range(len(arr)):
            if i <len(arr)-1:
                if i == 0:
                    num  = abs(arr[i+1] - arr[i])
                    print(num)
                else:
                    sets = abs(arr[i+1] - arr[i])
                    print(sets)
                    if sets < num:
                        num = sets
                        print("final;",num)
        
        for j in range(len(arr)):
            if j <len(arr)-1:
                if abs(arr[j+1] - arr[j]) == num:
                    temp = []
                    temp.append(arr[j])
                    temp.append(arr[j+1])             
                    c.append(temp)
        #print(c)
        return c
