from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World Again!'

@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/say/<string:name>')
def hello(name):
    print(name)
    return "Hi " + name

@app.route('/repeat/<int:num>/<string:name>')
def greeting(num, name):
    return f"{name*num}"

@app.route('/*')
def error_message():
    return f"Sorry! No response. Try again."

if __name__=="__main__": 
    app.run(host='localhost', port=5002)