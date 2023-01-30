from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it safe, keep it safe'

@app.route('/')
def main():
    print("Got Post Info")
    print(request.form)
    if "counter" in session:
        print('Key exists!')
        session["counter"] += 1
    else:
        print("key 'key_name' does NOT exist")
        session["counter"] = 0
    return render_template("index.html")

@app.route('/counter2')
def counter2():
    print("Got Post Info")
    print(request.form)
    if "counter" in session:
        print('Key exists!')
        session["counter"] += 2
    else:
        print("key 'key_name' does NOT exist")
        session["counter"] = 0
    return render_template("index.html")
            
@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)