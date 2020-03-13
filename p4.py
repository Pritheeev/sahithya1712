from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def stud(user):
	return render_template('students.html')
app.route ('/result', methods =['POST','GET'])
def result():
	if request.method =='POST':
		result = request.form
		return render.template("hello.html",result = result)
if __name__ == '__main__':
	app.run(debug = True, port=8082)

