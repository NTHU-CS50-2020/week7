from cs50 import SQL
from cs50 import sys
import csv

db=SQL("sqlite:///students.db")

if len(sys.argv) != 2:   #🎈sys.
    print("Usage: python import.py characters.csv")
    exit(1)

with open(sys.argv[1],"r")as file:
    reader=csv.DictReader(file)
    id=0
    for row in reader:
        nnn=row["name"].split()#名，字 分開
        if len(nnn)==3:
            first=nnn[0]
            middle=nnn[1]
            last=nnn[2]
        if len(nnn)==2:
            first=nnn[0]
            middle="none"
            last=nnn[1]
        h=row["house"]
        b=row["birth"]

        db.execute("INSERT INTO students (id, first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?, ?)", id, first, middle, last, h, b)
        id+=1