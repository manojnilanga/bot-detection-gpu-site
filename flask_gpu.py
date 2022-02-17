from flask import Flask, render_template,request
import psycopg2 # on ubuntu, sudo apt-get install libpq-dev, pip install psycopg2 / sudo pip3 install Psycopg2
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

app = Flask(__name__)

def middleof(text, left,right,multi=False):
    if(not multi):
        try:
            middle = text.split(left)[1].split(right)[0]
            return middle
        except:
            return ""
    else:
        right_text=text
        items=[]
        while(True):
            try:
                item = right_text.split(left)[1].split(right)[0]
                items.append(item)
                right_text = right_text.split(left,1)[1].split(right,1)[1]
            except:
                break
        return items

def check_bot(ip):
    print(ip)
    now = datetime.now()
    print(now)

    cursor.execute(sql.SQL("insert into ips(ip, datetime) values (%s, %s)"), [ip, now])
    conn.commit()
    print("Records inserted")

    check_date_time = now - timedelta(seconds=5)

    query = sql.SQL("select * from ips where ip= %s and datetime > %s")
    cursor.execute(query, (ip, check_date_time))

    result = cursor.fetchall()
    result_length = len(result)
    print("Result length: "+str(result_length))
    if(result_length>10):
        print("********** bot here **********")
        return True
    else:
        print("not a bot")
        return False

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('gpu.html')
    if request.method == 'POST':
        try:
            if(check_bot(request.remote_addr)):
                response_add_to_cart = {"status":"You are a bot"}
            else:
                now = datetime.now()
                # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                response_add_to_cart = {"status":"added to cart on "+str(now)}
            return render_template('gpu.html',response_add_to_cart=response_add_to_cart)
        except Exception as e:
            print("Error in POST method---> " + str(e))
            return render_template('gpu.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)