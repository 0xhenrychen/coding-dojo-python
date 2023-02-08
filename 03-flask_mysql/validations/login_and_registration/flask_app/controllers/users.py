from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route("/")
def index_page():
    return render_template("login.html")

@app.route("/login")
def login_page():
    return redirect("/")

@app.route("/logout")
def logout_page():
    session.clear()
    return redirect("/")

@app.route("/dashboard")
def dashboard_page():
    if "first_name" not in session:
        return redirect("/")
    return render_template("logged_in.html")

@app.route("/register", methods=["POST"])
def register_form():
    data = {
                "first_name": request.form["first_name"],
                "last_name": request.form["last_name"],
                "email": request.form["email"],
                "password1": request.form["password1"],
                "password2": request.form["password2"]
            }
    
    session["email"] = request.form["email"]
    session["first_name"] = request.form["first_name"]
    
    if not User.validate_user_register(data):
        return redirect("/")
    User.save_user(data)
    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login_form():
    data = {
                "email": request.form["email"],
                "password3": request.form["password3"]
            }
    if not User.validate_user_login(data):
        return redirect("/")
    this_user = User.get_user_by_email(data)
    session["first_name"] = this_user["first_name"]
    return redirect(f'/dashboard')

# @app.route("/create_order", methods=["POST"])
# def create_order():
#     data = {
#                 "customer_name": request.form["customer_name"],
#                 "cookie_type": request.form["cookie_type"],
#                 "number_of_boxes": request.form["number_of_boxes"]
#             }
        
#     if not Order.validate_order(data):
#         return redirect("/cookies/new")
#     Order.save(data)
#     return redirect("/cookies")

# @app.route("/cookies")
# def show_orders():
#     orders = Order.get_all()
#     return render_template("orders.html", orders = orders)

# @app.route("/cookies/new")
# def new_order():
#     return render_template("login.html")

# @app.route("/cookies/edit/<int:order_id>/")
# def edit_order_page(order_id):
#     data = {
#                 "id": order_id
#     }
#     this_order = Order.get_order_by_id(data)
#     return render_template("edit.html", order = this_order)

# @app.route("/order/edit", methods=["POST"])
# def edit_order():
#     data = {
#                 "order_id": request.form["order_id"],
#                 "customer_name": request.form["customer_name"],
#                 "cookie_type": request.form["cookie_type"],
#                 "number_of_boxes": request.form["number_of_boxes"]
#             }
#     if not Order.validate_order(data):
#         return redirect(f'/cookies/edit/{data["order_id"]}')
#     Order.update_order(data)
#     return redirect("/cookies")

# @app.route("/cookies/delete/<int:order_id>/")
# def delete_order(order_id):
#     Order.remove_order({"id": order_id})
#     return redirect("/cookies")