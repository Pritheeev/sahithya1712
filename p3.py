from flask import Flask, render_template
app = Flask(__name__)
@app.route('/hello/<int:id>')
def hello_name(id):
	count=0
	for i in range(2,id-1):
		if id%i==0:
			count=count+1
    if count==0:
		return "prime"
	else:
		return "not prime"
		
if __name__ == '__main__':
	app.run(debug = True)

