from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route("/")
def index():
    users = User.get_all()
    return render_template("index.html", users = users)

@app.route("/create_user", methods=["POST"])
def create_user():

    data = {
                "first_name": request.form["first_name"],
                "last_name": request.form["last_name"],
                "email": request.form["email"]
            }
    User.save(data)
    return redirect("/users")

@app.route("/users")
def show_users():
    users = User.get_all()
    return render_template("users.html", users = users)

@app.route("/users/<int:user_id>/destroy")
def delete_user(user_id):
    User.delete({"id": user_id})
    return redirect("/users")

@app.route("/users/<int:user_id>")
def show_user(user_id):
    this_user = User.get_by_id({"id": user_id})
    return render_template("user.html", user = this_user)

@app.route("/users/<int:user_id>/edit/")
def edit(user_id):
    data = {
                "id": user_id
    }
    this_user = User.get_by_id(data)
    return render_template("edit.html", user = this_user)

@app.route("/user/edit", methods=["POST"])
def edit_user():
    data = {
                "id": request.form["id"],
                "first_name": request.form["first_name"],
                "last_name": request.form["last_name"],
                "email": request.form["email"]
            }
    User.edit(data)
    # return redirect("/users")
    return redirect(f'/users/{data["id"]}')

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5008)