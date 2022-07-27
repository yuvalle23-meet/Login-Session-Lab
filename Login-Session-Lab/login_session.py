from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

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
		return render_template("home.html")


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', quote = login_session["quote"], author = login_session["author"], age = login_session["age"]) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)