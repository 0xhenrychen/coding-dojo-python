from django.shortcuts import render, redirect, render
import random

from datetime import datetime

def index(request):
    if "gold" and "activities" not in request.session:
        request.session["gold"] = 0
        request.session["activities"] = ""
    return render(request, "index.html")

def process_money(request):
    building = request.POST["building"]
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
    request.session["gold"] += gold_now
    
    if gold_now >= 0:
        message_now = f'<ul style = "color: green;"><li>Earned {gold_now} from the {building}! ({today_date} {today_time})</li></ul>'
        request.session["activities"] += message_now
    else:
        message_now = f'<ul style = "color: red;"><li>Entered the {building} and lost {gold_now} golds...ouch! ({today_date} {today_time})</li></ul>'
        request.session["activities"] += message_now
    return redirect("/")

def reset(request):
    del request.session["gold"]
    del request.session["activities"]
    return redirect("/")
