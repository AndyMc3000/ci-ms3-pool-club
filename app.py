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


# -------------- HELPER FUNCTIONS --------------
def is_logged_in():
    """
    This returns the user stored in the session or None
    """
    return session.get("user")


# homepage view
@app.route("/")
@app.route("/index")
def user():
    user = mongo.db.user.find()
    return render_template("index.html", user=user)


# current/active League table view
@app.route("/league")
def league():
    league = mongo.db.league.find()
    user = mongo.db.user.find()
    return render_template("league.html", league=league, user=user)


# historical/archive League tables view
@app.route("/archive")
def archive():
    league = mongo.db.league.find()
    archive = mongo.db.archive.find()
    if request.method == 'GET':
        return render_template("archive.html", league=league)


# club sign up page
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
            "firstname": request.form.get("firstname"),
            "surname": request.form.get("surname"),
            "nickname": request.form.get("nickname"),
            "telephone": request.form.get("telephone"), 
            # Default user values
            "admin": False,   
            "rank": "N/A",
            "points": 0,   
            "matches_played": 0,
            "matches_won": 0, 
            "matches_lost": 0,
            "games_won": 0, 
            "games_lost": 0,
            "entered_leagues": [] 
        }
        mongo.db.user.insert_one(register)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("email").lower()
        flash("Registration Successful!")
        return redirect(url_for("playerhome", firstname=session["user"]))

    return render_template("register.html")


# login page view
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if the user email exists in the db
        existing_user = mongo.db.user.find_one(
            {"email": request.form.get("email")})

        if existing_user:
            # ensures hashed password for the user matches the user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("email")
                    flash("Welcome, {}".format(request.form.get("email")))
                    return redirect(url_for(
                        "playerhome", firstname=session["user"]))
        
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# logout page view
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# player home page
@app.route("/player-home/<firstname>", methods=["GET", "POST"])
def playerhome(firstname):
    user_email = is_logged_in()
    if user_email:
        # Fetch the session user's first name from MongoDB
        user = mongo.db.user.find_one({"email": user_email})
        return render_template("player-home.html", user=user)
    return redirect(url_for("login"))


# add match view
@app.route("/add-match", methods=["GET", "POST"])
def addmatch():
    if request.method == "POST":
        match = {
            "player_one": request.form.get("player_one"),
            "player_two": request.form.get("player_two"),
            "player_one_games_won": request.form.get("player_one_games_won"),
            "player_two_games_won": request.form.get("player_two_games_won"),
            "date": request.form.get("date"),
            "league": request.form.get("league"),
            "referee": request.form.get("referee"),
            "createdby": session["user"]
        }
        mongo.db.matches.insert_one(match)
        flash("Match Successfully Added")
        return redirect(url_for("playerhome", firstname=session["user"]))

    return render_template("add-match.html",
                referee=mongo.db.user.find().sort("surname", 1),
                playerone=mongo.db.user.find().sort("surname", 1),
                playertwo=mongo.db.user.find().sort("surname", 1),
                league=mongo.db.league.find().sort("name", 1), )


# find contact details and league stats for another player
@app.route("/player-contact-info")
def playercontact():
    return render_template("player-contact-info.html", 
        playername=mongo.db.user.find().sort("surname", 1) )


# view player league statistics
@app.route("/player-active-results")
def mystats():
    player = mongo.db.user.find_one(
        {"email": session["user"]})
    return render_template("player-current-stats.html", player=player)


# view player match list
@app.route("/player-match-list")
def mymatchlist():
    return render_template("player-match-list.html")


# view player league statistics for past leagues
@app.route("/player-archive-results")
def playerarchive():
    return render_template("player-archive-results.html")


# edit player account details
@app.route("/player-edit-account", methods=["GET", "POST"])
def editaccount():
    player = mongo.db.user.find_one({"email": session["user"]})
    # if request.method == "POST":
        # update_player = {
            # "firstname": request.form.get("firstname"),
            # "surname": request.form.get("surname"),
            # "nickname": request.form.get("nickname"),
            # "email": request.form.get("email"),
            # "telephone": request.form.get("telephone"),
            # "password": request.form.get("password"),
            # "password2": request.form.get("password2")
        # }
        # mongo.db.matches.update({"_id": ObjectId(player)}, update_player)
        # flash("Account Successfully Updated")
        # return redirect(url_for("playerhome", firstname=session["user"]))
    
    # player_info = mongo.db.tasks.find_one({"_id": ObjectId(player)})
    return render_template("player-edit-account.html", user=player)


# admin home page
@app.route("/admin-home")
def adminhome():
    # user_email = is_logged_in()
    # if user_email:
        # player = mongo.db.user.find_one({"email": user_email})
        # if player.admin:
    return render_template("admin-home.html")
    # return redirect(url_for("playerhome"))


# add new league (admin view)
@app.route("/add-league", methods=["GET", "POST"])
def addleague():
    if request.method == "POST":
        league = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "start_date": request.form.get("startdate"),
            "end_date": request.form.get("enddate"),
            "participating_players": request.form.get("participants"),
        }
        mongo.db.league.insert_one(league)
        flash("League Added Successfully")
        return redirect(url_for("adminhome"))
  
    return render_template("add-league.html")


# add new player (admin view)
@app.route("/add-player", methods=["GET", "POST"])
def addplayer():
    if request.method == "POST":
        # check if username already exists in db
        current_user = mongo.db.user.find_one(
            {"email": request.form.get("email")})

        if current_user:
            flash("That Email / Username already exists")
            return redirect(url_for("addplayer"))

        addplayer = {
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "firstname": request.form.get("firstname"),
            "surname": request.form.get("surname"),
            "nickname": request.form.get("nickname"),
            "telephone": request.form.get("telephone")     
        }
        mongo.db.user.insert_one(addplayer)
        flash("Player Added Successfully")
        return redirect(url_for("adminhome"))

    return render_template("add-player.html")


# make a player an admin
@app.route("/add-admin", methods=["GET"])
def addadmin():
    return render_template("add-admin.html", playername=mongo.db.user.find().sort("surname", 1))
        

# edit/delete active league details (admin view)
@app.route("/edit-league", methods=["GET", "POST"])
def editleague():
    league = mongo.db.league.find()
        # if request.method == "GET":
            # selected_league = 
    return render_template("edit-league.html", league=league)
    # league = mongo.db.league.find().sort("name", 1))
        # if request.method == "POST":
            # update_league = {
                # "name": request.form.get("name"),
                # "description": request.form.get("description"),
                # "start_date": request.form.get("startdate"),
                # "end_date": request.form.get("enddate"),
                # "participating_players": request.form.get("participants"),
            # }
            # mongo.db.league.update_one(update_league)
            # flash("League Successfully Updated")
            # return redirect(url_for("adminhome")


# edit/delete player details (admin view)
@app.route("/edit-player", methods=["GET", "POST"])
def editplayer():
    player = mongo.db.user.find().sort("surname", 1)
    if request.method == "GET":
        selection = {
            "user": request.form.get("user"),
        }
        mongo.db.user.find(selection)

    return render_template("edit-player.html", user=selection, player=player)


# edit/delete match details (admin view)
@app.route("/edit-match")
def editmatch():
    matches = mongo.db.matches.find().sort("date", 1)
    return render_template("edit-match.html", matches=matches)


# -------------- EXCEPTION HANDLING --------------
@app.errorhandler(404)
def not_found_exception_handler(e):
    """
    Catch 404 not found
    """
    return render_template("error-404.html")


@app.errorhandler(Exception)
def generic_exception_handler(e):
    """
    Catch ANY other exception
    """
    return render_template("error-exception.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
