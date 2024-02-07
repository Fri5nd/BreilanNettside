from flask import Flask, render_template, request, url_for, redirect, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

# config 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "abc"
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


# class that defines the Users table in the database
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

# class that defines the Tournaments table in the database
class Tournaments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tournamentName = db.Column(db.String(150), unique=False, nullable=False)
    dato = db.Column(db.String(150), unique=False, nullable=False)
    organizer = db.Column(db.String(100), unique=False, nullable=False)
    time = db.Column(db.String(100), unique=False, nullable=False)
    linkToForms = db.Column(db.String(150), unique=False, nullable=False)

# initializes the database
with app.app_context():
    db.create_all()

# function that loads users
@login_manager.user_loader
def loader_user(user_id):
	return Users.query.get(user_id)

# route for the main page of the site
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
         return render_template('index.html')

# route for loging in a user
@app.route('/login', methods=['GET', 'POST'])
def login(): 
    flashed_message = get_flashed_messages(category_filter=['notAuth'])
    flashed_message = ','.join(flashed_message)


    if request.method == 'POST' and (request.form.get("usernameInput") != "" and request.form.get("passwordInput") != ""):
        user = Users.query.filter_by(username=request.form.get("usernameInput")).first()
        if user and user.password == request.form.get("passwordInput"):
            login_user(user)
            return redirect(url_for("index"))
        else:
            # Invalid username or password
            return render_template("login.html", error="Invalid username or password")

    elif request.method == 'POST' and (request.form.get("usernameInput") == "" or request.form.get("passwordInput") == ""):
        # Form not submitted correctly (e.g., missing username or password)
        return render_template("login.html", error="Please provide both username and password")

    elif flashed_message != None:
        return render_template("login.html", flashed_message=flashed_message)

    else:
        return render_template("login.html")

# route for logging out of your account
@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("index"))

@app.route('/add_tournament', methods=['GET', 'POST'])
def addTournament():
    if not current_user.is_authenticated:
        error="Du kan ikke endre på turneringer utenom å være pålogget!"
        flash(error, 'notAuth')
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            if 'tournamentNameForm' in request.form:
                tournament_Name = request.form['tournamentNameForm']
                tournament_Date = request.form['tournamentDateForm']
                tournament_Time = request.form['tournamentTimeForm']
                tournament_Organizer = request.form['tournamentOrganizerForm']
                tournament_Link = request.form['tournamentLinkForm']
                new_Tournament = Tournaments(tournamentName=tournament_Name, dato=tournament_Date, organizer=tournament_Organizer, time=tournament_Time, linkToForms=tournament_Link)
                db.session.add(new_Tournament)
                db.session.commit
        return render_template("add_tournament.html")

# Comment this out or remove before deploying website
# route for form that adds users
@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    if request.method == 'POST':
        user = Users(username=request.form.get("usernameInput"), password=request.form.get("passwordInput"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("addUser.html")

# runs the app on the flask development server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')