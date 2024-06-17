# Write a program that reads data from a CSV file and prints it to the console.

import csv
with open("file.csv",'r') as f:
    reader_object=csv.reader(f)
    for line in reader_object:
        print(line)


