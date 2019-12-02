class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        #print(widths)
        sum = 0
        line = 0
        for item in S:
            #print(item)
            #print(ord(item)-97)
            sum += widths[ord(item)-97]
            
            #left = S[S.index(item):]
            if sum > 100:
                #sum = sum - 100
                sum = widths[ord(item)-97]
                line +=1
            #print(sum)
            
        #print(left)
        if sum > 0:
            line +=1
        #print(sum,line)
        return [line,sum]
