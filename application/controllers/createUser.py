from application import app
from flask import render_template, request
from application.model.dao.uploadDAO import UploadDAO
from application.model.dao.createUserDAO import CreateUserDAO


@app.route("/register", methods=["POST", "GET"])

def register():
    if request.method == "POST":
        nome = request.form["nome"]
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        date = request.form["date"]
        file = request.files['photo']
        photo = file.filename
        user = CreateUserDAO()    
        user.create(nome, username, password, email, date, photo)
        upload = UploadDAO()
        upload.upload(file, "profile")
        return "OK"  
    return render_template("createUser.html")
