class Solution:
    def find(self,a,b):
        a=sorted(a)
        b=sorted(b)
        if len(b) - len(a) !=1:
            return -1
        else:
            mark=0
            for i in range(len(a)):
                if a[i] != b[i]:
                    mark=1
                    return b[i]
            if mark==0:
                return b[-1]  
            
        
            

if __name__ == '__main__':
    solution=Solution()
    s="abczefd"
    t="dbcazfde"
    print(solution.find(s,t))