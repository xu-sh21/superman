class Solution:
    def cal_time(self,title,s):
        term=[]
        for i in range(len(s)):
            if title in s[i]:
                term.append(s[i])
        total=0
        for i in range(len(term)):
            if "Enter" in term[i] and "Exit" in term[i+1]:
                """需要寻找每个字符串中的时间数字"""
                start_location=term[i].find("Enter")+6
                over_location=term[i+1].find("Exit")+5
                start=int(term[i][start_location:])
                over=int(term[i+1][over_location:])
                time=over-start
                total+=time
        return total
    
    def getTime(self,s):
        timelist={}
        titlelist=[]
        for i in range(len(s)):
            """寻找文件名称"""
            count=0
            while s[i][count] !=' ':
                count=count+1
            title=s[i][0:count]
            """如果不在，将文件名加入到文件列表中"""
            if title not in titlelist:
                titlelist.append(title)
            else:
                continue
        for i in range(len(titlelist)):
            """确定每个文件对应的时间"""
            time=solution.cal_time(titlelist[i],s)
            timelist[titlelist[i]]=time
        
        shuchu=[]
        for i in range(len(titlelist)):
            time_str=titlelist[i]+'|'+str(timelist[titlelist[i]])
            shuchu.append(time_str)
        
        return(shuchu)
                

if __name__ == '__main__':
    s=["F11 Enter 10","F2 Enter 18","F3 Enter 26","F2 Exit 19","F11 Exit 20","F3 Exit 29"]
    solution=Solution()
    print(solution.getTime(s))