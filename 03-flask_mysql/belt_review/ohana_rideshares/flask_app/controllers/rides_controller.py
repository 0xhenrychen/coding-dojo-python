from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, ride

@app.route("/rides/dashboard")
def rides_all_page():
    if "user_id" not in session:
        return redirect("/")
    rides_with_passengers = ride.Ride.connect_passengers_to_rides_join()
    return render_template("rides.html", rides = rides_with_passengers)

# @app.route("/recipes/view/<int:recipe_id>")
# def recipe_single_page(recipe_id):
#     data = {
#                 "id": recipe_id
#     }
#     one_recipe_with_user = recipe.Recipe.connect_user_to_recipe_join(data)
#     return render_template("recipe_view.html", recipe = one_recipe_with_user)

@app.route("/rides/new")
def create_ride_page():
    if "user_id" not in session:
        return redirect("/")
    return render_template("ride_request.html")

# @app.route("/recipes/edit/<int:recipe_id>")
# def update_recipe_page(recipe_id):
#     if "first_name" not in session:
#         return redirect("/")
#     data = {
#                 "id": recipe_id
#     }
#     one_recipe = recipe.Recipe.get_recipe_by_id(data)
#     return render_template("recipe_edit.html", recipe = one_recipe)

# @app.route("/recipes/delete/<int:recipe_id>")
# def delete_recipe(recipe_id):
#     data = {
#                 "id": recipe_id
#     }
#     recipe.Recipe.delete(data)
#     return redirect("/recipes")

@app.route("/create_ride_form", methods=["POST"])
def create_ride_form():
    data = {
            "destination": request.form["destination"],
            "pick_up_location": request.form["pick_up_location"],
            "rideshare_date": request.form["rideshare_date"],
            "details": request.form["details"],
            "user_id": session["user_id"]
    }
    print("this is the data:", data)
    if not ride.Ride.validate_create_ride_form(data):
        return redirect("/rides/new")
    
    # this_user = user.User.get_user_by_email(email)
    # data["user_id"] = this_user["id"]
    ride.Ride.save(data)
    return redirect("/rides/dashboard")

# @app.route("/update_recipe_form", methods=["POST"])
# def update_recipe_form():
#     data = {
#             "id": request.form["id"],
#             "name": request.form["name"],
#             "description": request.form["description"],
#             "instructions": request.form["instructions"],
#             "date": request.form["date"],
#             "under_30_mins": request.form["under_30_mins"]
#     }
#     if not recipe.Recipe.validate_create_recipe_form(data):
#         return redirect("/recipes/update")
#     recipe.Recipe.edit(data)
#     return redirect("/recipes")
