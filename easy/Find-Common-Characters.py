class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = []
        dict1 = {}
        #print(len(A))
        for item in A:
            for j in item:
                if j in dict1:
                    dict1[j] += 1
                else:
                    dict1[j] = 1
        
        print(dict1)
        #print(len(A))
        temp = []
        for key, value in dict1.items():
            count = 0
            cb = 0
            temp_list = []
            for it in A:
                if key in it:
                    count +=1
                    times = 0
                    for nums in it:
                        if key == nums:
                            times+=1
                    #print(times)
                    temp_list.append(times)
            mini = min(temp_list)
            #print(mini)
            if count == len(A):
                if mini > 1:
                    for t in range(mini):
                        temp.append(key)
                else:
                    temp.append(key)
        #print(temp)
        return temp
