#Write a python program that checks if two strings are anagrams of each other. 

def check(s1,s2):
    if len(s1)!=len(s2):
        print("not anagrams")
        return
    for c in s1:
        if s1.count(c)!=s2.count(c):
            print("not anagrams")
            return
    print("the strings are anagrams")
s1=input("enter string 1: ")
s2=input("enter string two: ")
check(s1,s2)