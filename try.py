ransomNote="aac"
magazine="abcdefg"

a=list(ransomNote)
b=list(magazine)


mark=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            del b[j]
            mark+=1
            break


if mark==len(a):
    print("True")
else:
    print("False")        