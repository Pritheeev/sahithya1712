from flask import Flask
app = Flask(__name__)
@app.route('/hello/<int:age>') 
def sum_1(age):
	sum=0
	while age>0 :
		n=age%10
		sum=sum+n
		age=age//10
	return 'Sum %d ' %sum
	
if __name__ =='__main__':
	app.run(debug = True)
