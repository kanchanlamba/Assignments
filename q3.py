#Write a python program that calculates the factorial of a given number

def fact(num):
    if num<0:
        print("Negative number , can not find factorial")
    if num==0:
        return 1
    return num*fact(num-1)

n=int(input("Enter the number : "))
print(fact(n))