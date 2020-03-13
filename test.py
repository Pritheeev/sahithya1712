from flask import Flask, render_template, request,redirect,url_for,session,logging,flash
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'new-password'
app.config['MYSQL_DB'] = 'db'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql = MySQL(app)

@app.route('/searchf',methods=['GET','POST'])
def searchf():
    # if request.method == "POST":
    #     details = request.form
    #     uname = details['nu']
    #     cur=mysql.connection.cursor()
    count=0
    proname='Sahithya'
    cur6=mysql.connection.cursor()
    cur6.execute("INSERT INTO searchf(value,count) VALUES (%s,%s)",(proname,count))
    mysql.connection.commit()
    cur6.close()
        # cur.execute("SELECT image from sahithya where image_id=%s",[uname])
        # data=cur.fetchone()
        # return render_template('extra.html')
    return render_template('extra.html')

if __name__ == '__main__':
    app.run(debug = True )