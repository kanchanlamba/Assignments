# Write a program that asks the user for their birth year and calculates their age.

import datetime 
def age(year):
    present_year=datetime.date.today().year
    age=present_year-year
    return age
year=int(input("enter birth year "))
print(age(year))





