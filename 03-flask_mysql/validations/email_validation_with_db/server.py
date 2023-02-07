from flask_app import app
from flask_app.controllers import users

# from flask import Flask, render_template, request, redirect
# import the class from user.py
# don't need - from user import User
# don't need - app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5006)