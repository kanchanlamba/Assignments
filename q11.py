# Write a python program that generates the first n numbers in the Fibonacci sequence.

n=int(input("Enter the number you want to print fibonacci sequence for : "))
a=0
b=1
i=0
c=0
while i<n:
    print(a,end=",")
    c=a+b
    a=b
    b=c
    i=i+1
        
print("Done!")



