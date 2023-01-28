from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberry = request.form['strawberry']
    blackberry = request.form['blackberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    num_fruits = int(strawberry) + int(blackberry) + int(raspberry) + int(apple)
    
    today = datetime.today()
    today_date = today.strftime('%B %d, %Y')
    today_time = today.strftime('%H:%M:%S')
    print(f'Today\'s date: {today_date} and time: {today_time}')
    print(request.form)
    print(f'Charging {first_name} {last_name} for {num_fruits} fruits.')
    
    return render_template("checkout.html", strawberry=strawberry, blackberry=blackberry,
                            raspberry=raspberry, apple=apple, first_name=first_name, last_name=last_name, student_id=student_id, num_fruits=num_fruits, today_date=today_date, today_time=today_time)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True, host='localhost', port=5002)