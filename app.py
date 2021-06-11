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
    """
    Function returns the Homepage view
    """
    # Returns Homepage view
    return render_template("index.html", user=user)


@app.route("/league")
def league():
    """
    Function returns the current League Table view and League Table
    statistics for all users
    """
    # Finds all Leagues in the league collection
    league = mongo.db.league.find()
    # Finds all users in the user collection
    user = mongo.db.user.find()
    # Renders league table page view
    return render_template("league.html", league=league, user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Function allows a site user to register to become a club
    member/registered user
    """
    if request.method == "POST":
        # Check if the users email address already exists
        # in MongoDB
        existing_user = mongo.db.user.find_one(
            {"email": request.form.get("email")})

        if existing_user:
            flash("That Email / Username already exists")
            # Redirects user to registration page if user email
            # already exists
            return redirect(url_for("register"))
        # list of values retrieved from registration form for
        # a new MongoDB user document
        register = {
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name"),
            "surname": request.form.get("surname"),
            "nickname": request.form.get("nickname"),
            "telephone": request.form.get("telephone"),
            # list of default user values for league statistics
            "admin": False,
            "points": 0,
            "matches_played": 0,
            "matches_won": 0,
            "matches_lost": 0,
            "games_won": 0,
            "games_lost": 0,
            "entered_leagues": []
        }
        # Creates new document in MongoDB user collection
        mongo.db.user.insert_one(register)

        # Puts the new user into a 'session' cookie, where the
        # session user is the user with the same email as the current user
        session["user"] = request.form.get("email").lower()
        flash("Registration Successful!")
        return redirect(url_for("player_home", first_name=session["user"]))

    return render_template("register.html", user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Function allows a registered to user to login, while checking
    that its email address and password match user values in MongoDB
    """
    if request.method == "POST":
        # Check to see if the user email exists in MongoDB
        existing_user = mongo.db.user.find_one(
            {"email": request.form.get("email")})

        if existing_user:
            # Ensures the hashed password for the user in MongoDB
            # matches the user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("email")
                flash("You have logged in as: {}".format(
                    request.form.get("email")))
                return redirect(url_for(
                    "player_home", first_name=session["user"]))

            else:
                # Returns message if password incorrect
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

    return render_template("login.html", user=user)


@app.route("/logout")
def logout():
    """
    Function allows a registered to logout
    """
    # Remove a user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/player-home", methods=["GET", "POST"])
def player_home():
    """
    Function returns the Player Homepage
    """
    # Fetch the session user's data from MongoDB
    user = mongo.db.user.find_one({"email": session["user"]})
    return render_template("player-home.html", user=user)


def post_save_match(match: dict, is_player_1: bool):
    """
    After the below add_match function is run, this function collects
    inputs from the Add Match Result form, calculates the points and
    match scores, and updates the players statistics in MongoDB
    (user) collection
    """
    player = "player_one" if is_player_1 else "player_two"
    # if statement calculates how player stats will be updated
    if is_player_1:
        games_won = int(request.form.get("player_one_games_won"))
        # TODO: Add function to also update games_won and
        # games_lost user values in MongoDB;
        # games_lost = int(request.form.get("player_two_games_won"))
    else:
        games_won = int(request.form.get("player_two_games_won"))
        # TODO: Add function to also update games_won and
        # games_lost user values in MongoDB;
        # games_lost = int(request.form.get("player_two_games_won"))
    update_data = {}
    update_data["$inc"] = {
        "matches_won" if games_won == 3 else
        "matches_lost": 1, "points": games_won + 1}
    # Update the player statistics in MongoDB user document
    mongo.db.user.update_one({"_id": ObjectId(match[player])}, update_data)


@app.route("/add-match", methods=["GET", "POST"])
def add_match():
    """
    Function allows a registered user to CREATE a new match
    result
    """
    if request.method == "POST":
        match = {
            # Player_one and player_two represent the user ObjectId's
            "player_one": request.form.get("player_one"),
            "player_two": request.form.get("player_two"),
            "player_one_games_won": request.form.get("player_one_games_won"),
            "player_two_games_won": request.form.get("player_two_games_won"),
            "date": request.form.get("date"),
            "league": request.form.get("league"),
            "referee": request.form.get("referee"),
            "created_by": session["user"]
        }
        mongo.db.matches.insert_one(match)
        # Calls the post save logic (see post_save_match) function above
        post_save_match(match, is_player_1=True)
        post_save_match(match, is_player_1=False)
        flash("Match Successfully Added")
        return redirect(url_for("player_home", first_name=session["user"]))

    return render_template(
        "add-match.html", user=user,
        referee=mongo.db.user.find().sort("surname", 1),
        player_one=mongo.db.user.find().sort("surname", 1),
        player_two=mongo.db.user.find().sort("surname", 1),
        league=mongo.db.league.find().sort("name", 1), )


@app.route("/player-current-stats")
def player_stats():
    """
    Function allows a registered user to READ their
    personal league statistics
    """
    league = mongo.db.league.find()
    player = mongo.db.user.find_one(
        {"email": session["user"]})
    return render_template(
        "player-current-stats.html", player=player,
        league=league, user=user)


@app.route("/player-edit-account", methods=["GET", "POST"])
def player_edit_account():
    """
    Function allows a registered user to edit and UPDATE
    their account details
    """
    player = mongo.db.user.find_one({"email": session["user"]})
    if request.method == "POST":
        update_player = {
            "first_name": request.form.get("first_name"),
            "surname": request.form.get("surname"),
            "nickname": request.form.get("nickname"),
            "email": request.form.get("email"),
            "telephone": request.form.get("telephone"),
            "password": generate_password_hash(request.form.get("password")),
            # These values Wil not be changed from what already
            # exits in the user collection
            "admin": bool(request.form.get("admin")),
            "points": int(request.form.get("points")),
            "matches_played": int(request.form.get("matches_played")),
            "matches_won": int(request.form.get("matches_won")),
            "matches_lost": int(request.form.get("matches_lost")),
            "games_won": int(request.form.get("games_won")),
            "games_lost": int(request.form.get("games_lost"))
        }
        mongo.db.user.update(player, update_player)
        flash("Account Successfully Updated")
        return redirect(url_for("player_home", first_name=session["user"]))

    return render_template(
        "player-edit-account.html", player=player, user=user,)


@app.route("/admin-home")
def admin_home():
    """
    Function returns the Admin homepage
    """
    user = mongo.db.user.find_one({"email": session["user"]})
    return render_template("admin-home.html", user=user)


@app.route("/add-league", methods=["GET", "POST"])
def add_league():
    """
    Function allows an Admin user to create a new
    league
    """
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


@app.route("/add-player", methods=["GET", "POST"])
def admin_register_user():
    """
    Function allows an Admin user to register a new
    user/club member
    """
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


@app.route("/select-league")
def select_league():
    """
    Function allows a user to select a league from a
    dropdown list so that the league can be edited
    using the edit_league function (see below)
    """
    league = mongo.db.league.find().sort("date", 1)
    return render_template("select-league.html", league=league, user=user)


@app.route("/edit_league/<league_id>", methods=["GET", "POST"])
def edit_league(league_id):
    """
    Function will UPDATE active league details (feature in admin view)
    """
    if request.method == "POST":
        league_update_data = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "start_date": request.form.get("start_date"),
            "end_date": request.form.get("end_date"),
            "participating_players": request.form.get("participants"),
        }
        mongo.db.league.update_one(
            {"_id": ObjectId(league_id)},
            {"$set": league_update_data})
        flash("League Successfully Updated")
        return redirect(url_for("admin_home"))
    league = mongo.db.league.find_one({"_id": ObjectId(league_id)})
    return render_template("edit-league.html", league=league, user=user)


@app.route("/delete_league/<league_id>")
def delete_league(league_id):
    """
    Function DELETE's a selected league from the league MongoDB collection
    """
    # TODO: Reset user stats when the league is deleted
    # (comment left here intentionally)
    mongo.db.league.remove({"_id": ObjectId(league_id)})
    # flash message when league is deleted
    flash("League Successfully Deleted")
    # redirects user to Admin Homepage
    return redirect(url_for("admin_home"))


# -------------- EXCEPTION HANDLING --------------
@app.errorhandler(404)
def not_found_exception_handler(e):
    """
    Catches 404 Page Not Found errors
    """
    print(e)
    return render_template("error-404.html", user=user)


@app.errorhandler(Exception)
def generic_exception_handler(e):
    """
    # Catches ANY other exception
    # """
    print(e)
    return render_template("error-exception.html", user=user)


# -------------- FUTURE FUNCTIONS/FEATURES --------------
# FUTURE RELEASE ONLY - Edit Player (Admin view);
@app.route("/edit-player", methods=["GET", "POST"])
def admin_edit_user():
    """
    Function allows an Admin to select a user from a dropdown
    box and then UPDATE user values, or DELETE the user
    """
    # TODO: READ user values and display in table on page. Add
    # function to allow and Admin to UDPATE the user values or DELETE the user
    player = mongo.db.user.find().sort("surname", 1)
    if request.method == "GET":
        selection = {
            "user": request.form.get("user"),
        }
        mongo.db.user.find(selection)

    return render_template("edit-player.html", user=selection, player=player)


# FUTURE RELEASE ONLY - Select a Match;
@app.route("/select-match")
def select_match():
    """
    Function returns the Select Match page view so
    that a user can select a match for editing on
    the Edit Match page (see below)
    """
    matches = mongo.db.matches.find().sort("date", 1)
    return render_template("select-match.html", user=user, matches=matches)


# FUTURE RELEASE ONLY - Edit a Match;
@app.route("/edit-match")
def edit_match():
    """
    Function returns the Edit Match page view and allows
    an Admin to edit the details of a Match
    """
    # TODO: Read selected Match data and present
    # in a form. A user can then UPDATE the values of a League
    # or DELETE a League.
    return render_template("edit-match.html", user=user)


# FUTURE RELEASE ONLY - Archive;
@app.route("/archive")
def archive():
    """
    Function returns the Archived League page view and
    allows a user to select an archive to view the
    League stats for that League
    """
    # TODO: Select archived league from dropdown list and present
    # league stats in table or seperate page view
    # (comment left here intentionally)
    league = mongo.db.league.find()
    # Finds all Leagues in the league collection
    archive = mongo.db.archive.find()
    # Retrieve selected archived league
    if request.method == 'GET':
        return render_template(
            "archive.html", league=league,
            archive=archive, user=user)


# FUTURE RELEASE ONLY - Player Details;
@app.route("/player-contact-info")
def player_contact():
    """
    Function selects a player from a dropdown and returns contact info
    and current league stats
    """
    # TODO: READ contact details and league stats for a player
    # from MongoDB and display in table on page
    # (comment left intentionally)
    return render_template(
        "player-contact-info.html", user=user,
        playername=mongo.db.user.find().sort("surname", 1))


# FUTURE RELEASE ONLY - Player Match List;
@app.route("/player-match-list")
def player_match_list():
    """
    Function allows a registered user to READ their
    personal match list, and view how many matches they have
    played against other players
    """
    # TODO: Add function to calculate how many matches a
    # player has played against all other players, and
    # show that number (0 matches, 1 match, or 2 matches)
    # in table on page
    user = mongo.db.user.find()
    return render_template("player-match-list.html", user=user)


# FUTURE RELEASE ONLY - Select an Admin;
@app.route("/select-admin")
def select_admin():
    """
    Function will allow an Admin to select
    a user and open the add_admin view
    """
    # TODO: On button select add_admin page will
    # open add-admin.html and pass the
    # selected user _id
    user = mongo.db.user.find().sort("first_name", 1)
    return render_template("select-admin.html", user=user)


# FUTURE RELEASE ONLY - Add an Admin;
@app.route("/add-admin", methods=["POST"])
def add_admin():
    """
    Function will allow an Admin to UPDATE
    the the Admin value for the selected users
    MongoDB document, giving them access to Admin
    Home
    """
    # TODO: Create function to allow an Admin to set the
    # selected users admn vaue to be 'true';
    # user = mongo.db.user.find()
    # if request.method == "POST":
    # make_admin = {
    # "admin": request.form.get("admin"),
    # }
    # mongo.db.user.update({"_id": ObjectId(user)}, make_admin)
    # flash("Site Admin Added Sucessfully")
    # return redirect(url_for("admin_home")
    return render_template("add-admin.html", user=user)


# FUTURE RELEASE ONLY - Player Archived Stats;
@app.route("/player-archive-results")
def player_archive_stats():
    """
    Function will allow a registered user to view
    their stats from a selected archived league
    """
    # TODO: Create function to READ and display
    # stats from an archived league selected from a
    # dropdown list of archived leagues on a yet to be created
    # select-archive-league.html. Stats should then be displayed
    # in a table on this page
    return render_template("player-archive-results.html", user=user)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
