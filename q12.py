# Write a python program that calculates the sum of the digits of a given number.

n=int(input("Enter a number : "))
temp=n
sum=0
while temp>0 :
    p=temp%10
    sum=sum+p
    temp=temp//10
    
print("The sum of digits is : ",sum)    
