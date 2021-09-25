from application import app
from flask import render_template, request, redirect, flash, url_for
from application.model.dao.uploadDAO import UploadDAO

@app.route("/postar", methods=['POST', 'GET'])

def postar():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        else:
            file = request.files['file']
            text = request.form["text"]
            if text == "" and file.filename == "":
                flash('Você está postando um arquivo vazio')
                return redirect(request.url)
            else:    
                upload = UploadDAO()
                filename = upload.upload(file, "post")
                return render_template('v1.html', name = filename, redirect=redirect, text=text)
    return render_template('v1.html')
