# TODO
from sys import argv, exit
import pandas as pd
from sqlalchemy import create_engine


if len(argv) != 2:
    exit("Usage: python roster.py Gryffindor")

engine = create_engine('sqlite:///students.db', echo=False)
sql = f"""SELECT * FROM students WHERE house = '{argv[1]}' ORDER BY last, first;"""
df = pd.read_sql(sql=sql, con=engine)

for i in range(len(df)):
    print(df['first'][i], end=" ")
    if df['middle'][i] is not None:
        print(df['middle'][i], end=" ")
    print(df['last'][i], end="")
    print(f', born {df.birth[i]}')
