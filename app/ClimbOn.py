from flask import Flask
from flask import Flask, flash, redirect, render_template, session, request, abort, url_for
import os
import tempfile
import os.path
from flask_login import LoginManager, UserMixin, login_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:////Users/richa/PycharmProjects/ClimbOn/app/tutorial.db', echo=True)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/richa/PycharmProjects/ClimbOn/app/tutorial.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view =

db = SQLAlchemy(app)
db.init_app(app)

@login_manager.user_loader
def load_user(id):
    from models import Users
    user = Users.query.filter_by(id=id).first()
    session['user'] = user.id
    print "Current : %s" % user
    session['user']
    print "aka %s" % user.username
    return user


@app.route('/')
def home():
    if not session.get('logged in'):
        # return render_template('index.html')
        return render_template('login.html')
    else:
        return "Hello! <a href='/logout'>Logout</a>"


@app.route('/index', methods=['POST', 'GET'])
def do_admin_login():
    # Testing registration
    #
    # if request.method == 'GET':
    #     username = request.get_data(uname)
    #     password = request.get_data(psw)
    #
    #
    #
    #
    #
    # # Testing Registration

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    # query = s.query(User).filter(User.username.in_([POST_USERNAME]), Users.password.in_([POST_PASSWORD]) )
    # result = query.first()
    from models import Users
    result = Users.query.filter_by(username=POST_USERNAME).first()
    print result
    if result:
        session['logged_in'] = True
        session['username'] = result.username
        print session['username']

        # Above doesn't work fully BUT IT DOES DO SOMETHING
        # session['id'] = '111'
        # PASSWORD DOES NOT WORK
        login_user(result)
        load_user(result.id)

        return render_template('index.html')
        # this doesn't work <--- Don't know why I made this comment. Sessions don't seem to work
    else:
        flash('wrong password')
    return home()

    # if request.method == 'POST':
    #
    #
    #
    #     return home()


@app.route('/index/climbingskillsstart')
def toprope():
    return render_template('climbingskillsstart.html')


@app.route('/index/climbingskills2')
def toprope2():
    return render_template('climbingskills2.html')


@app.route('/index/climbingskills3')
def climbingskills3():
    return render_template('climbingskills3.html')


@app.route('/index/climbingskills4')
def climbingskills4():
    return render_template('climbingskills4.html')


@app.route('/index/climbingskillsfinal')
def climbingskillsfinal():
    return render_template('climbingskillsfinal.html')


@app.route('/index/profile')
def profile():
    return render_template('profile.html')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


# @app.route("/test")
# def test():
#
#     POST_USERNAME = "python"
#     POST_PASSWORD = "python"
#
#     Session = sessionmaker(bind=engine)
#     s = Session()
#     query = s.query(User).filter(User.username.in_([POST_USERNAME]), Users.password.in_([POST_PASSWORD]))
#     result = query.first()
#     if result:
#         return "Object Found"
#     else:
#         return "object not found" + POST_USERNAME + "" + POST_PASSWORD


if __name__ == '__main__':
    app.secret_key = 'this_secret_key_of_mine'
    app.run(debug=True, host='0.0.0.0', port=5000)
