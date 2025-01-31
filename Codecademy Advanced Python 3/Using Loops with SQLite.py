import sqlite3

con = sqlite3.connect("titanic.db")
curs = con.cursor()

sum = 0
ages = curs.execute("SELECT Age FROM titanic;").fetchall()
for age in ages:
  if age[0] < 18:
    sum = sum + age[0]
  else:
    continue
print(sum)
