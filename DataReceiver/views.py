import os
from flask_api import status
from werkzeug import secure_filename
from DataReceiver import app
from flask import request, redirect, url_for

UPLOAD_FOLDER = '/tmp/UploadQueue'
ALLOWED_EXTENSIONS = set(['gz']);

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
        return 'Forbidden', status.HTTP_403_FORBIDDEN

@app.route('/api/1.0/registerWorkstation/<string:workstationGuid>',methods=['POST'])
def registerWorkstation(workstationGuid):
        return 'Thanks'

@app.route('/api/1.0/getServerName/<string:customerGuid>',methods=['GET'])
def getServerName(customerGuid):
        return ''

@app.route ('/api/1.0/uploadFile/', methods=['POST','GET'])
def upload_file():
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return filename, status.HTTP_200_OK
        else:
            return filename, status.HTTP_403_FORBIDDEN

