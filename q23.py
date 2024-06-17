# Write a program that converts temperature from Celsius to Fahrenheit 
# and vice versa based on user input.
ch=int(input("CHOOSE: 1 or 2\n"
"1: celsius to Fahrenheit\n"
"2: Fahrenheit to celsius\n")
)
if(ch==1):
    c=float(input("ENTER TEMP IN *c"))
    f=c*1.8+32
    print(c,"*C =",f,"*F")
elif ch==2:
    f=float(input("ENTER TEMP IN *f"))
    c=(f-32)/1.8
    print(f,"*F =",c,"*C")
else:
    print("INVALID CHOICE")