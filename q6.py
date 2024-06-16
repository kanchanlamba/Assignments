# Write a program that reads the content of a text file and prints it to the console
file=open("string.txt","w")
str=input("Enter a string : ")
file.write(str) 
file.close()
file=open("string.txt","r") 
content=file.read()
print("The content in file is : ",content) 
file.close() 
 
 
 
