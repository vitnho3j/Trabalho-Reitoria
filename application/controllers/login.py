from flask.helpers import url_for
from application import app
from application.model.entity.User import User
from application.model.dao.UserDAO import UserDAO
from flask import render_template, redirect, request
from flask_login import login_user, logout_user


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        pwd = request.form['password']

        user = User.query.filter_by(username=username).first()
    

        if not user or not UserDAO.verify_password(user, pwd):
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('home'))
    
    return render_template('login.html')



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))