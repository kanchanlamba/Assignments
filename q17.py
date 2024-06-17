#Write a program in python that converts a given string to title case (first letter of each word capitalized). 

s=input("enter a string ")

#using inbuilt function:
# print(s.title())

string_2=""
word=""
for c in s:
    if c!=" ":
        word+=c
    else:
        string_2+=word[0].upper()
        string_2+=word[1:]
        string_2+=" "
        word=""
if(word):
    string_2+=word[0].upper()
    string_2+=word[1:]
    string_2+=" "
    word=""
print(string_2)
        