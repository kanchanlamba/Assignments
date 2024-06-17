#Write a program that copies the contents of one text file to another. 
f=open("string.txt","r")
newf=open("file1.txt","w")
content=f.read()
newf.write(content)
newf.close()
f.close()