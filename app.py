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
#def is_logged_in():
    #"""
    #This returns the user stored in the session or None
    #"""
    #return session.get("user")


@app.route("/")
@app.route("/index")
def user():
    """
    Function returns the Homepage view
    """
    user = mongo.db.user.find() # finds all users in the user collection 
    return render_template("index.html", user=user)  # homepage view


@app.route("/league")
def league():
    """
    Function returns the current League Table view and League Table statistics for all users
    """
    league = mongo.db.league.find()  # finds all Leagues in the league collection
    user = mongo.db.user.find()  # finds all users in the user collection
    return render_template("league.html", league=league, user=user)  # current League table view


# FUTURE RELEASE
@app.route("/archive")
def archive():
    """
    Function returns the Archived League view
    """
    # TODO: Select archived league from dropdown list and present league stats in table (comment left here intentionally)
    league = mongo.db.league.find()  # finds all leagues in the league collection
    archive = mongo.db.archive.find()  # finds all Leagues in the league collection
    if request.method == 'GET':  # retrieve selected archived league
        return render_template("archive.html", league=league, 
        archive=archive, user=user) # historical/archive League tables view


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
            "first_name": request.form.get("first_name"),
            "surname": request.form.get("surname"),
            "nickname": request.form.get("nickname"),
            "telephone": request.form.get("telephone"), 
            # Default user values
            "admin": False,
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
        return redirect(url_for("player_home", first_name=session["user"]))

    return render_template("register.html", user=user)


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
                        "player_home", first_name=session["user"]))
        
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", user=user)

# logout page view
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# player home page
@app.route("/player-home", methods=["GET", "POST"])
def player_home():
    # Fetch the session user's first name from MongoDB
    user = mongo.db.user.find_one({"email": session["user"]})
    print(user)
    return render_template("player-home.html", user=user)


def post_save_match(match: dict, is_player_1: bool):
    player = "player_one" if is_player_1 else "player_two"
    # Updating for player
    if is_player_1:
        games_won = int(request.form.get("player_one_games_won"))
        games_lost = int(request.form.get("player_two_games_won"))
    else:
        games_won = int(request.form.get("player_two_games_won"))
        games_lost = int(request.form.get("player_one_games_won"))
    update_data = {}
    update_data["$inc"] = {"matches_won" if games_won == 3 else "matches_lost": 1,
                           "points": games_won + 1}
    # update_data["$set"] = {"matches_won": 1} # If you want to set data instead of update
    mongo.db.user.update_one({"_id": ObjectId(match[player])}, update_data)

# add match view
@app.route("/add-match", methods=["GET", "POST"])
def add_match():
    if request.method == "POST":
        match = {
            "player_one": request.form.get("player_one"), # this represents the ObjectId
            "player_two": request.form.get("player_two"), # this represents the ObjectId
            "player_one_games_won": request.form.get("player_one_games_won"),
            "player_two_games_won": request.form.get("player_two_games_won"),
            "date": request.form.get("date"),
            "league": request.form.get("league"),
            "referee": request.form.get("referee"),
            "created_by": session["user"]
        }
        mongo.db.matches.insert_one(match)
        # Post save logic
        post_save_match(match, is_player_1=True)
        post_save_match(match, is_player_1=False)
        flash("Match Successfully Added")
        return redirect(url_for("player_home", first_name=session["user"]))

    return render_template("add-match.html", user=user,
                referee=mongo.db.user.find().sort("surname", 1),
                player_one=mongo.db.user.find().sort("surname", 1),
                player_two=mongo.db.user.find().sort("surname", 1),
                league=mongo.db.league.find().sort("name", 1), )


# REMOVE ? find contact details and league stats for another player
@app.route("/player-contact-info")
def player_contact():
    return render_template("player-contact-info.html", playername=mongo.db.user.find().sort("surname", 1) )


# view player league statistics
@app.route("/player-current-stats")
def player_stats():
    league = mongo.db.league.find()
    player = mongo.db.user.find_one(
        {"email": session["user"]})
    return render_template("player-current-stats.html", player=player, league=league, user=user)


# view player match list
@app.route("/player-match-list")
def player_match_list():
    user = mongo.db.user.find()
    return render_template("player-match-list.html", user=user)


# REMOVE ? view player league statistics for past leagues
@app.route("/player-archive-results")
def player_archive_stats():
    return render_template("player-archive-results.html")


# edit player account details
@app.route("/player-edit-account", methods=["GET", "POST"])
def player_edit_account():
    player = mongo.db.user.find_one({"email": session["user"]})
    if request.method == "POST":
        update_player = {
            "first_name": request.form.get("first_name"),
            "surname": request.form.get("surname"),
            "nickname": request.form.get("nickname"),
            "email": request.form.get("email"),
            "telephone": request.form.get("telephone"),
            "password": request.form.get("password"),
            "password2": request.form.get("password2")
        }
        mongo.db.user.update({"_id": ObjectId(player)}, update_player)
        flash("Account Successfully Updated")
        return redirect(url_for("player_home", first_name=session["user"]))
    
    return render_template("player-edit-account.html", player=user)


# admin home page
@app.route("/admin-home")
def admin_home():
    user = mongo.db.user.find_one({"email": session["user"]})
    print(user)
    return render_template("admin-home.html", user=user)


# add new league (admin view)
@app.route("/add-league", methods=["GET", "POST"])
def add_league():
    if request.method == "POST":
        league = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "start_date": request.form.get("start_date"),
            "end_date": request.form.get("end_date"),
            "participating_players": request.form.get("participants"),
        }
        mongo.db.league.insert_one(league)
        flash("League Added Successfully")
        return redirect(url_for("admin_home"))
  
    return render_template("add-league.html", user=user)


# add new player (admin view)
@app.route("/add-player", methods=["GET", "POST"])
def admin_register_user():
    if request.method == "POST":
        # check if username already exists in db
        current_user = mongo.db.user.find_one(
            {"email": request.form.get("email")})

        if current_user:
            flash("That Email / Username already exists")
            return redirect(url_for("admin_register_user"))

        admin_register_user = {
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name"),
            "surname": request.form.get("surname"),
            "nickname": request.form.get("nickname"),
            "telephone": request.form.get("telephone"),
            # Default user values
            "admin": False,
            "points": 0,   
            "matches_played": 0,
            "matches_won": 0, 
            "matches_lost": 0,
            "games_won": 0, 
            "games_lost": 0,
            "entered_leagues": []      
        }
        mongo.db.user.insert_one(admin_register_user)
        flash("Player Added Successfully")
        return redirect(url_for("admin_home"))

    return render_template("add-player.html", user=user)



# select a player to make an admin
@app.route("/select-admin")
def select_admin():
    user = mongo.db.user.find().sort("first_name", 1)
    return render_template("select-admin.html", user=user)


# make a player an admin
@app.route("/add-admin", methods=["POST"])
def add_admin():
    #user = mongo.db.user.find()
    #if request.method == "POST":
        #make_admin = {
            #"admin": request.form.get("admin"),
        #}
        #mongo.db.user.update({"_id": ObjectId(user)}, make_admin)
        #flash("Site Admin Added Sucessfully")
        #return redirect(url_for("admin_home")
    return render_template("add-admin.html", user=user)
    

# select a league from a dropdown box
@app.route("/select-league")
def select_league():
    league = mongo.db.league.find().sort("date", 1)
    return render_template("select-league.html", league=league, user=user)


@app.route("/edit_league/<league_id>", methods=["GET", "POST"])
def edit_league(league_id):
    """
    Edit active league details (admin view)
    """
    if request.method == "POST":
        league_update_data = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "start_date": request.form.get("start_date"),
            "end_date": request.form.get("end_date"),
            "participating_players": request.form.get("participants"),
        }
        mongo.db.league.update_one({"_id": ObjectId(league_id)}, {"$set": league_update_data})
        flash("League Successfully Updated")
        return redirect(url_for("admin_home"))
    league = mongo.db.league.find_one({"_id": ObjectId(league_id)})
    return render_template("edit-league.html", league=league, user=user)

# delete a selected league
@app.route("/delete_league/<league_id>")
def delete_league(league_id):
    # TODO: Reset user stats when the league is deleted (comment left here intentionally)
    mongo.db.league.remove({"_id": ObjectId(league_id)}) # remove league based on its _id
    flash("League Successfully Deleted") # flash message when league is deleted
    return redirect(url_for("admin_home")) # redirects user to Admin Homepage


# REMOVE ? edit/delete player details (admin view)
@app.route("/edit-player", methods=["GET", "POST"])
def admin_edit_user():
    player = mongo.db.user.find().sort("surname", 1)
    if request.method == "GET":
        selection = {
            "user": request.form.get("user"),
        }
        mongo.db.user.find(selection)

    return render_template("edit-player.html", user=selection, player=player)


# REMOVE ? select a match for editing (admin view)
@app.route("/select-match")
def select_match():
    matches = mongo.db.matches.find().sort("date", 1)
    return render_template("select-match.html", matches=matches)


# REMOVE ? edit/delete match details (admin view)
@app.route("/edit-match")
def edit_match():
    return render_template("edit-match.html",)


# -------------- EXCEPTION HANDLING --------------
@app.errorhandler(404)
def not_found_exception_handler(e):
    """
    Catchs 404 page not found
    """
    print(e)
    return render_template("error-404.html")


@app.errorhandler(Exception)
def generic_exception_handler(e):
    """
    Catchs ANY other exception
    """
    print(e)
    return render_template("error-exception.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
