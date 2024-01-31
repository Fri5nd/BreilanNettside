from flask import Flask, render_template, request, url_for, redirect
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
    if request.method == 'POST' and (request.form.get("usernameInput") != "" or request.form.get("passwordInput") != ""):
        user = Users.query.filter_by(username=request.form.get("usernameInput")).first()
        if user and user.password == request.form.get("passwordInput"):
            login_user(user)
            return redirect(url_for("index"))
        else:
            # Invalid username or password
            return render_template("login.html", error="Invalid username or password")
            print(error)
    else:
        # Form not submitted correctly (e.g., missing username or password)
        return render_template("login.html", error="Please provide both username and password")
        print(error)
    return render_template("login.html")

# route for logging out of your account
@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("index"))

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
    app.run(debug=True)