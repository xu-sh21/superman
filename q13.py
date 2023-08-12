class Solution:
    def cal_time(self,title,s):
        term=[]
        for i in range(len(s)):
            if title in s[i]:
                term.append(s[i])
        total=0
        for i in range(len(term)):
            if "Enter" in term[i] and "Exit" in term[i+1]:
                start=int(term[i][9:])
                over=int(term[i+1][8:])
                time=over-start
                total+=time
        return total
    
    def getTime(self,s):
        timelist={}
        titlelist=[]
        for i in range(len(s)):
            title=s[i][0:2]
            if title not in titlelist:
                titlelist.append(title)
            else:
                continue
        for i in range(len(titlelist)):
            time=solution.cal_time(titlelist[i],s)
            timelist[titlelist[i]]=time
        
        shuchu=[]
        for i in range(len(titlelist)):
            time_str=titlelist[i]+'|'+str(timelist[titlelist[i]])
            shuchu.append(time_str)
        
        return(shuchu)
                

if __name__ == '__main__':
    s=["F1 Enter 10","F2 Enter 18","F3 Enter 26","F2 Exit 19","F1 Exit 20","F3 Exit 29"]
    solution=Solution()
    print(solution.getTime(s))