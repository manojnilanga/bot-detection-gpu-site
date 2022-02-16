import psycopg2 # on ubuntu, sudo apt-get install libpq-dev, pip install psycopg2
from psycopg2 import sql
from datetime import datetime, timedelta

#establishing the connection
conn = psycopg2.connect(
   database="gpu", user='postgres', password='postgres', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

request_ip = '14.11.11.1111'
now = datetime.now()
print("now =", now)

# cursor.execute('''INSERT INTO ips(ip, datetime) VALUES ('10.20.21.100', '2022-02-03 14:10:20')''')

# cursor.execute('''INSERT INTO ips(ip, datetime) VALUES ('''+request_ip+''', '''+str(now)+''')''')

# query = sql.SQL("insert into ips(ip, datetime) VALUES ({request_ip}, {date_time})").format(
#     table=sql.Identifier('ips'),
#     request_ip=sql.Identifier(request_ip),
#     date_time=sql.Identifier(str(now)))
# cursor.execute(query)

# working insert query
cursor.execute(sql.SQL("insert into ips(ip, datetime) values (%s, %s)"),[request_ip, now])

# Commit your changes in the database
conn.commit()
print("Records inserted........")

cursor.execute('''SELECT * from ips''')


check_date_time = now - timedelta(seconds = 10)
print(check_date_time)

query = sql.SQL("select * from ips where ip= %s and datetime > %s")
cursor.execute(query, ('14.11.11.1111',check_date_time))

#Fetching 1st row from the table
result = cursor.fetchall()
print(result)

#Closing the connection
conn.close()