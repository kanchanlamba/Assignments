# Write a python program that checks if a substring is present in a given string.

str=input("Enter a string : ")
substr=input("Enter the substring you are looking for : ")
result=str.find(substr)
if result==-1:
    print("Sub-string is not present.")
else:
    print("Sub-string is present.")    
