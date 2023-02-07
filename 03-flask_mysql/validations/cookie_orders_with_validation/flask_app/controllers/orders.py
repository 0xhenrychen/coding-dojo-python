from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.order import Order

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_order", methods=["POST"])
def create_order():
    data = {
                "customer_name": request.form["customer_name"],
                "cookie_type": request.form["cookie_type"],
                "number_of_boxes": request.form["number_of_boxes"]
            }
        
    if not Order.validate_order(data):
        return redirect("/cookies/new")
    Order.save(data)
    return redirect("/cookies")

@app.route("/cookies")
def show_orders():
    orders = Order.get_all()
    return render_template("orders.html", orders = orders)

@app.route("/cookies/new")
def new_order():
    return render_template("index.html")

@app.route("/cookies/edit/<int:order_id>/")
def edit_order_page(order_id):
    data = {
                "id": order_id
    }
    this_order = Order.get_order_by_id(data)
    return render_template("edit.html", order = this_order)

@app.route("/order/edit", methods=["POST"])
def edit_order():
    data = {
                "order_id": request.form["order_id"],
                "customer_name": request.form["customer_name"],
                "cookie_type": request.form["cookie_type"],
                "number_of_boxes": request.form["number_of_boxes"]
            }
    if not Order.validate_order(data):
        return redirect(f'/cookies/edit/{data["order_id"]}')
    Order.update_order(data)
    return redirect("/cookies")

@app.route("/cookies/delete/<int:order_id>/")
def delete_order(order_id):
    Order.remove_order({"id": order_id})
    return redirect("/cookies")

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5008)