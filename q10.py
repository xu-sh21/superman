class solution:
    def judge(self,a,b):
        if len(a) == len(b):
            a_list=list(a)
            b_list=list(b)
        
            a_list_odd=[]
            a_list_even=[]
            for i in range(0,len(a_list),2):
                a_list_odd.append(a_list[i])
            for i in range(1,len(a_list),2):
                a_list_even.append(a_list[i])
        
            b_list_odd=[]
            b_list_even=[]
            for i in range(0,len(b_list),2):
                b_list_odd.append(b_list[i])
            for i in range(1,len(b_list),2):
                b_list_even.append(b_list[i])
                
            if sorted(a_list_odd)==sorted(b_list_odd) and sorted(a_list_even)==sorted(b_list_even):
                return "Yes"
            else:
                return "No"
        else:
            return "No"
if __name__=="__main__":
    s='abcdr'
    t='cdabr'
    Solution=solution()
    print(Solution.judge(s,t))