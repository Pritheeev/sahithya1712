from flask import Flask,redirect,url_for
app = Flask(__name__)

#@app.route('/hello/<name>')    for string
#@app.route('/hello/<int:age>') for integer
@app.route('/admin')
def hello_world():
	return 'Hello'

@app.route('/guest/<name1>')
def hello_guest(name1):
	return 'Hello guest %s ' %name1

@app.route('/user/<name>')
def hello_user(name):
	if name == 'admin':
		return redirect(url_for('hello_world'))
	else:
		return redirect(url_for('hello_guest',name1=name))
		app.run(debug=True)
if __name__ =='__main__':
	app.run(debug = True)
