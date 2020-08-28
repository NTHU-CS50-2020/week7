import sys, cs50

if len(sys.argv) != 2:
    print("Usage: python roster.py house")
    exit(1)

db = cs50.SQL("sqlite:///students.db")
reader = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last,first", sys.argv[1])

for row in reader:
    #print(row)#{'id': 6, 'first': 'Colin', 'middle': 'none', 'last': 'Creevey', 'house': 'Gryffindor', 'birth': 1981}
    middle=row['middle']
    if row['middle']=='none':
        print("{0} {1},born {2}".format(row['first'],row['last'],row['birth']))
    else:
        print("{0} {1} {2},born {3}".format(row['first'],middle,row['last'],row['birth']))