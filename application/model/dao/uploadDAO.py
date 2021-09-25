import os
from application import app
from werkzeug.utils import secure_filename

class UploadDAO():

    def upload(self, file, route):

        if route == "post":
            UPLOAD_FOLDER = "C:\\Users\\Vitor\\Desktop\\Trabalho Reitoria\\Ambiente_Virtual\\application\\view\\statics\\posts"
            ALLOWED_EXTENSIONS = {'txt', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'pdf'}
            

        if route == "profile":
            UPLOAD_FOLDER = "C:\\Users\\Vitor\\Desktop\\Social Game\\Ambiente_Virtual\\application\\view\\statics\\profile"
            ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
            

        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

        def allowed_file(filename):
            return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return filename