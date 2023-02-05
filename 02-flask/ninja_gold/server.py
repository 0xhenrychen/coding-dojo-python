from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "this_is_the_secret_key"

import random
from datetime import datetime

@app.route("/")
def main():
    if "gold" and "activities" not in session:
        session["gold"] = 0
        session["activities"] = ""
    return render_template("index.html", activities = session["activities"])

@app.route("/process_money", methods=["POST"])
def process_money():
    building = request.form["building"]
    gold_now = 0
    message_now = ""
    
    today = datetime.today()
    today_date = today.strftime('%B %d, %Y')
    today_time = today.strftime('%H:%M')
    
    if building == "farm":
        gold_now += random.randint(10, 20)
    elif building == "cave":
        gold_now += random.randint(5, 10)
    elif building == "house":
        gold_now += random.randint(2, 5)
    else:
        gold_now += random.randint(-50, 50)
    session["gold"] += gold_now
    
    if gold_now >= 0:
        message_now = f'<ul style = "color: green;"><li>Earned {gold_now} from the {building}! ({today_date} {today_time})</li></ul>'
        session["activities"] += message_now
    else:
        message_now = f'<ul style = "color: red;"><li>Entered the {building} and lost {gold_now} golds...ouch! ({today_date} {today_time})</li></ul>'
        session["activities"] += message_now
    return redirect("/")

@app.route("/destroy_session")
def reset():
    session.clear()
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug = True, host="localhost", port=5008)
