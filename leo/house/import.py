from sys import argv, exit
from cs50 import SQL
import csv

import collections

db = SQL("sqlite:///students.db")

if (len(argv) != 2):
    exit("Usage: python import.py data.csv sequence.txt")

with open(argv[1] , "r")as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["name"].split()
        
        if(len(name) == 3):
            first = name[0]
            middle = name[1]
            last = name[2]
        
        elif(len(name) == 2):
            first = name[0]
            middle = None
            last = name[1]

        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first, middle, last, row["house"], row["birth"])
