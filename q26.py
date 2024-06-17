#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
given=input("enter a string: ")
pre=input("enter prefix: ")
suf=input("enter suffix: ")
f=0

for i in range(0,len(pre)):
    if len(pre)>len(given):
        f=1
        print("IT DOES NOT STARTS WITH GIVEN PREFIX")
        break
    if(given[i]!=pre[i]):
        f=1
        print("IT DOES NOT STARTS WITH GIVEN PREFIX")
        break
    
if f==0:
    print("IT STARTS WITH GIVEN PREFIX")
f=0
for j in range(-1,-len(suf)-1,-1):
    if len(suf)>len(given):
        f=1
        print("IT DOES NOT END WITH GIVEN SUFFIX")
        break
    if(given[j]!=suf[j]):
        f=1
        print("IT DOES NOT END WITH GIVEN SUFFIX")
        break
if f==0:
    print("IT ENDS WITH GIVEN SUFFIX")