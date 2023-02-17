from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, ride

@app.route("/rides/dashboard")
def rides_all_page():
    if "user_id" not in session:
        return redirect("/")
    this_user = user.User.get_user_by_id({"user_id": session["user_id"]})
    request_rides = ride.Ride.get_all_with_no_driver()
    booked_rides = ride.Ride.get_all_with_driver()
    return render_template("rides.html", user = this_user, requests = request_rides, booked = booked_rides)

@app.route("/rides/new")
def create_ride_page():
    if "user_id" not in session:
        return redirect("/")
    return render_template("ride_request.html")

@app.route("/rides/driver/<int:ride_id>")
def assign_driver_to_ride(ride_id):
    if "user_id" not in session:
        return redirect("/")
    data = {
            "ride_id": ride_id,
            "driver_id": session["user_id"]
    }
    ride.Ride.assign_driver_to_ride(data)
    return redirect("/rides/dashboard")

@app.route("/rides/details/<int:ride_id>")
def view_ride_page(ride_id):
    if "user_id" not in session:
        return redirect("/")
    this_ride = ride.Ride.get_ride_and_driver_by_id({"ride_id": ride_id})
    return render_template("ride_view.html", ride = this_ride)

@app.route("/rides/cancel/<int:ride_id>")
def cancel_ride(ride_id):
    data = {
                "ride_id": ride_id,
                "driver_id": None
    }
    ride.Ride.remove_driver_from_ride(data)
    return redirect("/rides/dashboard")

@app.route("/rides/edit/<int:ride_id>")
def edit_ride_page(ride_id):
    print("does it make it here")
    if "user_id" not in session:
        return redirect("/")
    print("does it make it here")
    this_ride = ride.Ride.get_ride_and_driver_by_id({"ride_id": ride_id})
    return render_template("ride_edit.html", ride = this_ride)

@app.route("/rides/delete/<int:ride_id>")
def delete_ride(ride_id):
    data = {
                "id": ride_id
    }
    ride.Ride.delete(data)
    return redirect("/rides/dashboard")

@app.route("/create_ride_form", methods=["POST"])
def create_ride_form():
    data = {
            "destination": request.form["destination"],
            "pick_up_location": request.form["pick_up_location"],
            "rideshare_date": request.form["rideshare_date"],
            "details": request.form["details"],
            "user_id": session["user_id"]
    }
    if not ride.Ride.validate_create_ride_form(data):
        return redirect("/rides/new")
    ride.Ride.save(data)
    return redirect("/rides/dashboard")

@app.route("/edit_ride_form", methods=["POST"])
def edit_ride_form():
    data = {
            "destination": request.form["destination"],
            "pick_up_location": request.form["pick_up_location"],
            "rideshare_date": request.form["rideshare_date"],
            "details": request.form["details"],
            "user_id": session["user_id"]
    }
    if not ride.Ride.validate_create_ride_form(data):
        return redirect("/rides/new")
    ride.Ride.save(data)
    return redirect("/rides/dashboard")