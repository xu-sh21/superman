class Solution:
    def judge(self,list,number):
        mark=0
        for i in range(len(list)):
            if number in range(list[i][0],list[i][1]):
                mark=1
                return "True"
                break
        if mark == 0:
            return "False"
            
        
                

if __name__ == '__main__':
    List=[[100,1100],[1000,2000],[5500,6600]]
    number=6000
    solution=Solution()
    print(solution.judge(List,number))