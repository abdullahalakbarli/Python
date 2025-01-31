import sqlite3

con = sqlite3.connect("titanic.db")
curs = con.cursor()

one = curs.execute("SELECT * FROM titanic").fetchone()
print(one)
ten = curs.execute("SELECT * FROM titanic").fetchmany(10)
print(ten)
all_rows = curs.execute("SELECT * FROM titanic").fetchall()
all_survived = curs.execute("""SELECT * FROM titanic WHERE Survived == '1';""").fetchall()
print(all_survived)
