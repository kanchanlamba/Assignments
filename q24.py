#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
num1=float(input("enter number1: "))
num2=float(input("enter number2: "))
op=input("Enter an operator (+, -, *, /): ")
if op=="+":
    res=num1+num2
    print(num1,"+",num2,"=",res)
elif op=="-":
    res=num1-num2
    print(num1,"-",num2,"=",res)
elif op=="*":
    res=num1*num2
    print(num1,"*",num2,"=",res)
elif op=="/":
    res=num1/num2
    print(num1,"/",num2,"=",res)
else:
    print("INVALID CHOICE")