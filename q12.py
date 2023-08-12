class Solution:
    def cal(self,A,B):
        if len(A) != len(B):
            return -1
        else:
            mark=0
            for i in range(len(A)):
                mark+=A[i]*B[i]
            return mark
                

if __name__ == '__main__':
    A=[1,2]
    B=[3,4]
    solution=Solution()
    print(solution.cal(A,B))
                        