class Solution:
    def cal(self,list):
        result = [0]*len(list)
        for i in range(len(list)):
            result[i]=Solution.mul(list,i)
        
        return result
    def mul(list,num):
        a=1
        for i in range(len(list)):
            if i != num:
                a*=list[i]
        return a
            
        
                

if __name__ == '__main__':
    solution=Solution()
    A=[1,2,3,4]
    print(solution.cal(A))