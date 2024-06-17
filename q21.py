#Write a python program that counts the occurrences of a specific element in a list. 
n=int(input("enter element to search for: "))
ans=0
l=[5,7,9,3,4,5,2,1,9,0,5,4,3,3,3,2,1,8,0,6,4,3,7]
for i in l:
    if i==n:
        ans+=1
print("ans: ",ans)