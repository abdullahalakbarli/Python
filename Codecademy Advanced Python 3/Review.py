import sqlite3

con = sqlite3.connect('titanic.db')
curs = con.cursor()
n_row = curs.execute("""SELECT * FROM new_table WHERE username = 'stephB423'""").fetchone()
print(n_row)
con.close()
