from sys import argv, exit
from cs50 import SQL
import csv

db = SQL("sqlite:///students.db")

if(len(argv) != 2):
    exit("Usage: python import.py data.csv sequence.txt")

query_data = db.execute(f"SELECT first,middle,last,birth FROM students WHERE house = '{argv[1]}' order by last, first")

for i in range(len(query_data)):
    if(query_data[i]["middle"] == None):
        print(query_data[i]["first"] ,end = " ")
        print(query_data[i]["last"] ,end = ",")
        print(f'born {query_data[i]["birth"]}')
    else:
        print(query_data[i]["first"] ,end = " ")
        print(query_data[i]["middle"] ,end = " ")
        print(query_data[i]["last"] ,end = ",")
        print(f'born {query_data[i]["birth"]}')