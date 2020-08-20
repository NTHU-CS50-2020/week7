# TODO
import pandas as pd
from sqlalchemy import create_engine
from sys import argv, exit

if len(argv) != 2:
    exit("Usage: python import.py characters.csv")

df = pd.read_csv(argv[1])
df['first'] = df['name'].apply(lambda x: x.split(' ')[0])
df['middle'] = df['name'].apply(lambda x: x.split(' ')[1] if len(x.split(' ')) == 3 else None)
df['last'] = df['name'].apply(lambda x: x.split(' ')[-1])
header = list(df.columns.values)
header = header[-3:] + header[1:-3]
df = df[header].reset_index().rename(columns={"index": "id"})
engine = create_engine('sqlite:///students.db', echo=False)
df.to_sql('students', con=engine, if_exists='append', index=False)
print(df.head())
