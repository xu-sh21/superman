class Solution:
    def search(self,target,list):
        if len(list) <2:
            return -1
        else:
            mark=0
            for i in range(len(list)-1):
                for j in range(i+1,len(list)):
                    if list[i]+list[j]<target:
                        sum=list[i]+list[j]
                        mark=max(mark,sum)
            return mark

if __name__ == '__main__':
    array=[1,3,5,11,7,3,2,11,14,23,45,56]
    target=70
    solution=Solution()
    print(solution.search(target,array))
                        