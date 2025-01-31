from start import helper
helper()
import sqlite3

con = sqlite3.connect("titanic.db")
curs = con.cursor()

curs.execute("""INSERT INTO new_table VALUES ('Stephanie Bready', 37, 'stephB423', 30.00)""")
con.commit()
con.close()
