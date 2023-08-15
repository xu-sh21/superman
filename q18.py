class Solution:
    def spell(self,list):
        shuchu=[]
        line=["qwertyuiop","asdfghjkl","zxcvbnm"]
        for i in range(len(list)):
            string=list[i]
            string=string.lower()
            location=[0]*len(string)
            for j in range(len(string)):
                for k in range(len(line)):
                    if string[j] in line[k]:
                        location[j]=k
            """确定字符串每个字母所在位置，形成列表"""
            result = solution.judge(location)
            if result==1:
                shuchu.append(string)
        return shuchu
    
    def judge(self,list):
        mark=0
        for m in range(0,len(list)-1):
            for n in range(m+1,len(list)):
                if list[m] != list[n]:
                    mark=1
        if mark==0:
            return 1
        else:
            return 0
            
                

if __name__ == '__main__':
    solution=Solution()
    word=["word","Alaska","Dad","Bnm","AsdAghK"]
    print(solution.spell(word))