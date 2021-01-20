from os import getcwd
from os import path

from datetime import datetime
from datetime import timedelta

from flask import Flask
from flask import flash
from flask import jsonify
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask import url_for

from application.dao.accountdao import AccountDAO
from application.dao.filedao import FileDAO

app = Flask(__name__)
app.secret_key = 'wckdev'
app.permanet_session_lifetime = timedelta(minutes=15)
app.config['UPLOAD_FOLDER'] = path.join(getcwd(), 'files')

upload_folder = app.config['UPLOAD_FOLDER']

db = path.join(getcwd(), 'databases/db.db')

accountDAO = AccountDAO(db)
fileDAO = FileDAO(db)

@app.route('/')
def index():
	if 'nickname' in session:
		return redirect(url_for('home'))
	else:
		return render_template('index.jinja', title='Inicio', app_name='Files - Login')

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		session.permanet = True
		nickname = request.form['nickname']
		secret_key = request.form['secret_key']
		if accountDAO.login(nickname, secret_key):
			session['nickname'] = nickname
			flash(f'Bienvenido <b>{nickname}</b>!', 'success')
			return redirect(url_for('home'))
		elif nickname == '' or secret_key == '':
			flash('Campos vacios!', 'danger')
			return redirect(url_for('index'))
		else:
			flash('Usuario no encontrado/registrado', 'danger')
			return redirect(url_for('index'))
	else:
		if 'nickname' in session:
			return redirect(url_for('home'))
		return redirect(url_for('index'))

@app.route('/logout')
def logout():
	if 'nickname' in session:
		session.pop('nickname', None)
		flash('Sesión cerrada!', 'warning')
		return redirect(url_for('index'))
	else:
		return redirect(url_for('index'))

@app.route('/home')
def home():
	if 'nickname' in session:
		return render_template('home/index.jinja', title='Files', app_name='Files')
	else:
		return redirect(url_for('index'))

@app.route('/uploadFile', methods=['POST'])
def fileUpload():
	if 'nickname' in session:
		file = request.files['file']
		type = file.filename.split('.')[1]
		name = datetime.now().strftime('%Y-%m-%d.%H.%M.%S') + '.' + type
		url = path.join(upload_folder, name)
		file.save(url)
		data = (name, type, url)
		if fileDAO.uploadFile(data):
			flash('Archivo subido!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Error al subir el archivo!', 'danger')
			return redirect(url_for('home'))
	else:
		return redirect(url_for('index'))

@app.errorhandler(403)
def error403(e):
	return render_template('errors/error.jinja', title='403', error=403), 403

@app.errorhandler(404)
def error404(e):
	return render_template('errors/error.jinja', title='404', error=404), 404

@app.errorhandler(405)
def error405(e):
	return render_template('errors/error.jinja', title='405', error=405), 405

@app.errorhandler(410)
def error410(e):
	return render_template('errors/error.jinja', title='410', error=410), 410

@app.errorhandler(500)
def error500(e):
	return render_template('errors/error.jinja', title='500', error=500), 500
