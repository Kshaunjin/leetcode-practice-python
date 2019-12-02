class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        listed = []
        for i in emails:
            if i.find('@')!=-1:
                a,b =i.split('@',2)
                #print(a,b)
                c=a.split('+')[0]
                c = c.replace('.','')
                #print(c)
                ans = c+'@'+b
                print(ans)
                if ans not in listed:
                    listed.append(ans)
            
        return len(listed)
