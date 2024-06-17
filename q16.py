# Write a program in python that counts the frequency of each character in a string.

def ch(s):
    set_char=set()
    for char in s:
        set_char.add(char)
    for ch in set_char:
        n=s.count(ch)
        print(ch,": ",n)
        
s=input("enter a string ")
ch(s)