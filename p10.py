from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'new-password'
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        cur = mysql.connection.cursor()
        cur.execute("INSERT into login(username, password) VALUES (:username,:password)",{"username":username,"password":password})
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('sample.html')


if __name__ == '__main__':
    app.run(debug = True)