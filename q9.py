def find(a):
    b=[]
    for i in range(len(a)):
        if search(b,a[i])==0:
            b.append(a[i])
        else:
            b.remove(a[i])
    print(b)

def search(list,num):
    mark=0
    for i in range(len(list)):
        if num==list[i]:
            return 1
            break
        mark+=1
    if mark==len(list):
        return 0
    
      
a=[1,2,5,6,6,2]
find(a)