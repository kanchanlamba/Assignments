#Write a python program that takes a list of numbers and returns their sum
l=eval(input("enter the list of numbers"))
s=0
for num in l:
    s+=num
print("sum is : ",s," using sum(): ",sum(l))