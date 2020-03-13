
from flask import Flask, render_template
app = Flask(__name__)

		

@app.route('/hello', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        details = request.form
        uname = details['username']
        password = details['password']
	diction={1:'sahithya',2:'abithaa'}
        if uname in diction:
  		return 'valid'
	else:
		return 'invalid'
	return render_template("signin.html")
        

if __name__ == '__main__':
	app.run(debug = True)
