from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    dojos = Dojo.get_all_dojos()
    ninjas = Ninja.get_all_ninjas()
    print(">>> All dojos:",dojos)
    print(">>> All ninjas:",ninjas)
    return render_template("index.html", dojos = dojos, ninjas = ninjas)
    # return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", dojos = dojos)

@app.route("/dojos/<int:dojo_id>")
def ninjas_by_dojo(dojo_id):
    data = {
    "id": dojo_id
    }
    all_ninjas_by_dojo = Ninja.get_ninjas_by_dojo(data)
    return render_template("dojos_all.html", all_ninjas_by_dojo = all_ninjas_by_dojo)

@app.route("/ninjas")
def ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("ninjas.html", dojos = dojos)

@app.route("/create_dojo", methods =["POST"])
def create_dojo():
    data = {
            "name": request.form["name"]
    }
    Dojo.save_dojo(data)
    return redirect("/")

@app.route("/create_ninja", methods =["POST"])
def create_ninja():
    data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "age": request.form["age"],
            "dojo_id": request.form["dojo_id"]
    }
    Ninja.save_ninja(data)
    return redirect("/")

@app.route("/ninjas/edit/<int:ninja_id>")
def edit_page(ninja_id):
    data = {
                "id": ninja_id
    }
    this_ninja = Ninja.get_ninja_by_id(data)
    return render_template("ninja_edit.html", ninja = this_ninja)

@app.route("/ninja/edit", methods=["POST"])
def edit_ninja():
    data = {
            "id": request.form["ninja_id"],
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "age": request.form["age"]
        }
    Ninja.update_ninja(data)
    
    # dojo_by_ninja = Dojo.get_dojo_by_ninja(id)
    # print(">>>results",dojo_by_ninja)
    
    return redirect(f'/dojos')
    # return redirect(f'/dojos/{dojo_id}')

@app.route("/dojos/<int:dojo_id>/<int:ninja_id>")
def delete_ninja(dojo_id, ninja_id):
    data = {
    "id": ninja_id
    }
    Ninja.remove_ninja(data)
    return redirect(f'/dojos')
