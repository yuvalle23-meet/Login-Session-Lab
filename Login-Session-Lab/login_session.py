from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


UPLOAD_FOLDER = '/home/student/Documents/GitHub/Login-Session-Lab/Login-Session-Lab/static'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

login_session={'quote':[], 'age':[], 'author':[]}

@app.route('/', methods=["GET", "POST"]) # What methods are needed?
def home():
	
	if request.method == "POST":
		
		try:

			login_session['quote'].append(request.form["quote"])
			login_session['author'].append(request.form["author"])
			login_session['age'].append(request.form["age"])

		
			if login_session['age'] != "":
				return redirect(url_for('thanks'))
			else:
				return render_template("home.html")

		except:
			return redirect(url_for('error'))

	else:
		return render_template("home.html", filename = login_session['file'])


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', quote = login_session["quote"], author = login_session["author"], age = login_session["age"]) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
login_session['file'] = []

@app.route('/file', methods = ["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        print("wewwewe")
        # check if the post request has the file part
        if 'file1' not in request.files:
            flash('No file part')
            return redirect(url_for('home'))
        file = request.files['file1']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('home'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            login_session['file'].append(filename)
            return redirect(url_for('home', filename = login_session['file']))
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
	app.run(debug=True)