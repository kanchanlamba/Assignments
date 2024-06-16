# Write a python program that checks whether a given number is even or odd

choice="YES"
while(choice.upper()=="YES"):
    num=int(input("Enter the number  : "))
    if num%2==0:
        print("EVEN")
    else:
        print("ODD")
    choice=input("DO YOU WANT TO CHECK FOR MORE NUMBERS (YES/NO) : ")
    