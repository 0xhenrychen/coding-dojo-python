from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it safe, keep it safe'

import random

@app.route("/")
def main():
    if "random_number" not in session:
        session["random_number"] = random.randint(1, 100)
        session["message"] = ""
    return render_template("index.html", message = session["message"])

@app.route("/guess", methods=["POST"])
def guess():
    session["guess_number"] = int(request.form["number_guess"])
    print("Random number is:", session["random_number"])
    message = ""
    print("Your guess is:", session["guess_number"])
    
    
    if session["guess_number"] > session["random_number"]:
        print("Guess number is HIGHER than random number.")
        session["message"] = f'Too high!'
    elif session["guess_number"] < session["random_number"]:
        print("Guess number is LOWER than random number.")
        session["message"] = f'Too low!'
    else:
        print("Guess number is EQUAL to random number.")
        session["message"] = f'{session["random_number"]} was the number!'
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)