class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        temp = []
        domain = []
        c = ''
        for item in cpdomains:
            a = item.split(' ')
            #print(a[0])
            #print(a[1])
            c_list = a[1].split('.')
            #print(len(c_list))
            #print(c_list[-3])
            for i in range(len(c_list)):
                b = len(c_list) -1
                dd = c_list[b-i]
                if c != '':
                    dd = dd +'.'+ c
                #print(dd)
                if dd not in temp:
                    temp.append(dd)
                    c = dd
            c = ''
            for t in temp:
                if t not in domain:
                    domain.append(t)
            temp = []
        print(domain)
        
        ans_list = []
        for it in domain:
            count = 0
            for i in cpdomains:
                a = i.split(' ')
                #print(len(it))
                #print(a[1][-len(it):])
                if it == a[1][-len(it):]:
                    #print(a[0])
                    count += int(a[0])
            #print(it,count)
            ans = str(count) + ' ' + it
            #print(ans)
            ans_list.append(ans)
        return ans_list
