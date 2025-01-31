# Import module 
import sqlite3


# Task 1: Create connection object
con = sqlite3.connect("hotel_booking.db")

# Task 2: Create cursor object
cur = con.cursor()

# Task 3: View first row of booking_summary
print(cur.execute("""SELECT * FROM booking_summary""").fetchone())

# Task 4: View first ten rows of booking_summary 
print(cur.execute("""SELECT * FROM booking_summary""").fetchmany(10))

# Task 5: Create object bra and print first 5 rows to view data
bra = cur.execute("""SELECT * FROM booking_summary WHERE country = 'BRA'""").fetchall()

# Task 6: Create new table called bra_customers
cur.execute("""CREATE TABLE IF NOT EXISTS bra_customers (
                   num INTEGER,
                   hotel TEXT,
                   is_cancelled INTEGER,
                   lead_time INTEGER,
                   arrival_date_year INTEGER,
                   arrival_date_month,
                   arrival_date_day_of_month INTEGER,
                   adults INTEGER,
                   children INTEGER,
                   country TEXT,
                   adr REAL,
                   special_requests INTEGER)""")
# Task 7: Insert the object bra into the table bra_customers 
bra_customers = cur.executemany("""INSERT INTO bra_customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", bra)

# Task 8: View the first 10 rows of bra_customers
print(cur.execute("""SELECT * FROM bra_customers""").fetchmany(10))

# Task 9: Retrieve lead_time rows where the bookings were canceled
lead_time_can = cur.execute("""SELECT lead_time FROM bra_customers WHERE is_cancelled = 1;""").fetchall()

# Task 10: Find average lead time for those who canceled and print results
sum_1 = 0
for num in lead_time_can:
  sum_1 = sum_1 + num[0]

# Task 11: Retrieve lead_time rows where the bookings were not canceled
lead_time_can_not = cur.execute("""SELECT lead_time FROM bra_customers WHERE is_cancelled = 0;""").fetchall()

# Task 12: Find average lead time for those who did not cancel and print results
sum_2 = 0
for num in lead_time_can_not:
  sum_2 = sum_2 + num[0]

# Task 13: Retrieve special_requests rows where the bookings were canceled
special_requests_is_cancelled = cur.execute("""SELECT special_requests FROM bra_customers WHERE is_cancelled = 1;""").fetchall()

# Task 14: Find total speacial requests for those who canceled and print results
count = 0
for num in special_requests_is_cancelled:
  count = count + num[0]

# Task 15: Retrieve special_requests rows where the bookings were not canceled
special_requests_is_not_cancelled = cur.execute("""SELECT special_requests FROM bra_customers WHERE is_cancelled = 0;""").fetchall()

# Task 16: Find total speacial requests for those who did not cancel and print results
count_cancelled = sum(num[0] for num in special_requests_is_cancelled)
count_not_cancelled = sum(num[0] for num in special_requests_is_not_cancelled)
print(f"count_cancelled: {count_cancelled}")
print(f"count_not_cancelled: {count_not_cancelled}")
# Task 17: Commit changes and close the connection
con.commit()
con.close()
