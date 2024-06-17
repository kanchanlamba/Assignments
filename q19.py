#Write a python program that removes all punctuation from a given string.
import string
s1=input("enter the string")
s2=""
for c in s1:
    if c not in string.punctuation :
        s2+=c

s1=s2
print(s2)