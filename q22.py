#Write a python program that counts the occurrences of a specific element in a list.
l=eval(input("enter the list"))
c=0
num=int(input("enter the element"))
for i in l:
    if i==num:
        c+=1
print(num," occurs ",c," times ")