from flask import Flask, render_template, request,redirect,url_for,session,logging,flash,make_response
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'new-password'
app.config['MYSQL_DB'] = 'open'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql = MySQL(app)




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        details = request.form
        uname = details['username']
        password = details['password']
        role=details['role']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO login(username, password1,role) VALUES (%s, %s,%s)", (uname, password,role))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('login'))
    return render_template('signup1.html')

@app.route('/login',methods =['GET', 'POST'])
def login():
    if request.method == "POST":
        details = request.form
        uname = details['username']
        password = details['password']
        role=details['role']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM login")
        data = cur.fetchall()
        resp = make_response(render_template('signin1.html'))
        resp.set_cookie('User', uname)
        return render_template('open2.html', n = uname,p=password,r =role,login=data)
    return render_template('signin1.html')
    

@app.route('/login1')
def login1(id1):
    #cur = mysql.connection.cursor()
    #cur.execute("SELECT * FROM login where username = %s",(id1))
    #data = cur.fetchall()
        #userdata=(cur.execute("Select username FROM login ").fetchone
        #passdata=(cur.execute("Select password FROM login ").fetchone
        #cur.close()
        #if userdata is None:
        #    return render_template('signin1.html')
        #else:
        #   for x in passdata:
        #        if x==password :
        #            return 'Login successful'
        #        else:
        #            return render_template('signin1.html')
        #return redirect(url_for('home'))
    return render_template('open2.html')
    #return render_template('signin1.html')
    
@app.route('/doctor/<string:id1>',methods=['GET','POST'])
def doctor(id1):
    if request.method == "GET":
        cur=mysql.connection.cursor()
        cur.execute("SELECT patient from app where doctor =%s",[id1])
        data = cur.fetchall()
    return render_template('open5.html',patients=data)

@app.route('/patient',methods=['GET','POST'])
def patient():
    if request.method == "GET":
        cur=mysql.connection.cursor()
        cur.execute("SELECT username from login where role ='doctor'")
        data = cur.fetchall()
    return render_template('open3.html',data1=data)

@app.route('/appointment',methods=['GET','POST'])
def appointment():
    if request.method == "POST":
        details = request.form
        doc = details['doctor']
        pat = details['patient']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO app(doctor, patient) VALUES (%s,%s)", (doc,pat))
        mysql.connection.commit()
        cur.close()
        return'Appointment Made'
    return render_template('appoint.html')


if __name__ == '__main__':
    app.run(debug = True )