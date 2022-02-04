from flask import Flask, render_template,request
from datetime import datetime

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

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('gpu.html')
    if request.method == 'POST':
        try:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("date and time =", dt_string)
            response_add_to_cart = {"status":"added to cart on "+str(dt_string)}
            return render_template('gpu.html',response_add_to_cart=response_add_to_cart)
        except Exception as e:
            print("Error in POST method---> " + str(e))
            return render_template('gpu.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)