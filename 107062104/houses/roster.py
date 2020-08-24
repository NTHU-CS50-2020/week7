import sys, cs50

if len(sys.argv) != 2:
    print("Usage: python roster.py Gryffindor")
    exit(1)

db = cs50.SQL("sqlite:///students.db")
reader = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first", sys.argv[1])

for row in reader:
    middle = "" if row["middle"] is None else " "+row["middle"]
    print(f'{row["first"]}{middle} {row["last"]}, born {row["birth"]}')