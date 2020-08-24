import sys, csv, cs50

if len(sys.argv) != 2:
    print("Usage: python import.py characters.csv")
    exit(1)

db = cs50.SQL("sqlite:///students.db")

with open(sys.argv[1], "r") as input:
    reader = csv.DictReader(input)
    id = 0
    for row in reader:
        names = row["name"].split()
        first = names[0]
        last = names[1] if len(names) == 2 else names[2]
        middle = None if len(names) == 2 else names[1]
        db.execute("INSERT INTO students (id, first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?, ?)", id, first, middle, last, row["house"], row["birth"])
        id += 1

