class Solution:
    def cal(self,num):
       start=1
       length=1
       count=9
       while num > length*count:
            num -= length * count
            length +=1
            count *=10
            start *=10
       start += (num-1)//length
       return int(str(start)[(num-1)% length])
        
            
        
                

if __name__ == '__main__':
    solution=Solution()
    
    print(solution.cal(11))