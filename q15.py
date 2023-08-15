class Solution:
    def cal(seif,list,):
        list=sorted(list)
        odd=0
        even=0
        for i in range(len(list)):
            odd+=abs(list[i]-(2*i+1))
            even+=abs(list[i]-(2*i+2))
        return min(odd,even)
        
        
            
        
                

if __name__ == '__main__':
    solution=Solution()
    list=[1,6,7,8,9]
    print(solution.cal(list))