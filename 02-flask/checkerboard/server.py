from flask import Flask, render_template
app = Flask(__name__)                     
    
@app.route('/')                           
def root():
    return render_template('index.html')

if __name__=="__main__": 
    app.run(host='localhost', port=5005)         

# @app.route('/success')
# def success():
#     return "success"

# @app.route('/hello/<name>')
# def hello(name):
#     print(name)
#     return "Hello, " + name

# @app.route('/users/<username>/<id>')
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return f"username: {username}, id: {id}"

# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response

