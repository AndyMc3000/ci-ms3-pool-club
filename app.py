import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/index")
def user():
    user = mongo.db.user.find()
    return render_template("index.html", user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.user.find_one(
            {"email": request.form.get("email")})

        if existing_user:
            flash("That Email / Username already exists")
            return redirect(url_for("register"))

        register = {
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("firstName"),
            "surname": request.form.get("surname"),
            "nickname": request.form.get("nickname"),
            "mobile_number": request.form.get("telephone")     
        }
        mongo.db.user.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("email")
        flash("Registration Successful!")
        return redirect(url_for("profile", email=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if the user email exists in the db
        existing_user = mongo.db.user.find_one(
            {"email": request.form.get("email")})

        if existing_user:
            # ensure our hashed password for the user matches the user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("email")
                    flash("Welcome, {}".format(request.form.get("email")))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<first_name>", methods=["GET", "POST"])
def profile(first_name):
    # grab the session user's username from db
    usernamefirts_name = mongo.db.user.find_one(
        {"first_name": session["user"]})["first_name"]
    return render_template("profile.html", first_name=first_name)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
