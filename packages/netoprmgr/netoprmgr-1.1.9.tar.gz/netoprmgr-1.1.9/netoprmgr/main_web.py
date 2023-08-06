import os
import pkg_resources
from flask import Flask, render_template

import urllib.request
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

BASE_DIR = pkg_resources.resource_filename('netoprmgr', '')
os.chdir(BASE_DIR)
CAPT_DIR = os.path.join(BASE_DIR,'static','capture')
DATA_DIR = os.path.join(BASE_DIR,'static','data')

ALLOWED_EXTENSIONS_CAPT = set(['txt', 'log'])
ALLOWED_EXTENSIONS_DATA = set(['xlsx',])

app.secret_key = "!qw3ezxc7gsj4nn1j23kkf9"
app.config['UPLOAD_FOLDER_CAPT'] = CAPT_DIR
app.config['UPLOAD_FOLDER_DATA'] = DATA_DIR

def allowed_file_capt(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_CAPT

def allowed_file_data(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_DATA

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/device_data/upload")
def device_data_upload_page():
    return render_template('device_data_upload_page.html')

@app.route('/device_data/upload', methods=['POST'])
def device_data_upload():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file_data(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER_DATA'], filename))
			flash('File successfully uploaded')
			return redirect('/device_data/result')
		else:
			flash('Allowed file type is xlsx')
			return redirect(request.url)

@app.route('/device_data/result')
def data_download():
	return render_template('device_data_download.html')


@app.route("/log/upload")
def log_upload_page():
    return render_template('log_upload_page.html')

@app.route('/log/upload', methods=['POST'])
def log_upload():
	if request.method == 'POST':
        # check if the post request has the files part
		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')
		for file in files:
			if file and allowed_file_capt(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER_CAPT'], filename))
			flash('Logs successfully uploaded')
		return redirect('/log/upload')

@app.route('/capture_log')
def capture_log():
	from main_cli import MainCli
	MainCli.captureDevice()
	return redirect('/capture_log/download')

@app.route('/capture_log/download')
def capture_log_download():
	return render_template('capture_log_download.html')

@app.route('/report/generate')
def report_generate_page():
	return render_template('report_generate.html')

@app.route('/report/result')
def report_generate():
	from main_cli import MainCli
	MainCli.createReport()
	return render_template('report_download.html')

@app.route('/env/generate')
def env_generate_page():
	return render_template('env_generate.html')

@app.route('/env/result')
def env_generate():
	from main_cli import MainCli
	MainCli.showEnvironment()
	return render_template('env_download.html')

@app.route('/log')
def log_delete_page():
	return render_template('log_delete.html')

@app.route('/log/delete')
def log_delete():
	from main_cli import MainCli
	MainCli.deleteCapture()
	return redirect('/log/upload')

if __name__ == "__main__":
    app.run(debug=True)