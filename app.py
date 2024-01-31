from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

# config 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "abc"
db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)



class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

class Tournaments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tournamentName = db.Column(db.String(150), unique=False, nullable=False)
    dato = db.Column(db.String(150), unique=False, nullable=False)
    organizer = db.Column(db.String(100), unique=False, nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'GET':
         return render_template('index.html')

@app.route('/adduser', methods=['GET', 'POST'])
def add_User():
    if request.method == 'POST':
        user = Users(username=request.form.get("username"), password=request.form.get("password"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index"))


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)