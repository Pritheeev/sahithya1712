from flask import Flask, render_template, request,redirect,url_for,session,logging,flash
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'new-password'
app.config['MYSQL_DB'] = 'db'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql = MySQL(app)


@app.route('/',methods =['GET', 'POST'])
def image():
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO image values(LOAD_FILE('/home/hp/Pictures/webscrap.png')")
    mysql.connection.commit()
    cur.close()
    return render_template('messages.html')


if __name__ == '__main__':
    app.run(debug = True )