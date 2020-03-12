from flask import Flask, render_template, request,redirect,url_for,session,logging,flash
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'new-password'
app.config['MYSQL_DB'] = 'db'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql = MySQL(app)



@app.route('/')
def front():
    return render_template('home.html')
    
@app.route('/aboutus')
def aboutus():
	return render_template('aboutus.html')

#STUDENT PART
	
@app.route('/sregister', methods=['GET', 'POST'])
def sregister():
    if request.method == "POST":
        details = request.form
        uname = details['username']
        password = details['password']
        cpass = details['cpassword']
        profname=details['profname']
        about =details['about']
        qualification=details['qualification'] 
        dob =details['dob']
        phone =details['phone']
        email =details['email']
        uniname = details['uniname']
        course= details['course']
        gdate = details['gdate']
        schname = details['schname']
        gsdate = details['gsdate']
        place1=details['place1']
        design = details['design']
        duration = details['duration']
        descr = details['descr']
        place2=details['place2']
        design1 = details['design1']
        duration1 = details['duration1']
        descri = details['descri']
        skill1 = details['skill1']
        skill2 = details['skill2']
        skill3 = details['skill3']
        skill4 = details['skill4']
        skill5 = details['skill5']
        aeo1=details['aeo1']
        aeo2=details['aeo2']
        aeo3=details['aeo3']
        cur=mysql.connection.cursor()
        cur1 = mysql.connection.cursor()
        cur2 = mysql.connection.cursor()
        cur3 = mysql.connection.cursor()
        cur4 = mysql.connection.cursor()
        if password == cpass:
            cur.execute("INSERT INTO login(username, password) VALUES (%s, %s)", (uname, password))
            cur4.execute("INSERT INTO profile( profname , username , about , qualification , dob , phone ,email) VALUES (%s,%s,%s,%s,%s,%s,%s)",( profname , uname , about , qualification , dob , phone ,email))
            cur1.execute("INSERT INTO info(username,uniname,course,gdate,schname,gsdate) VALUES (%s,%s,%s,%s,%s,%s)",(uname,uniname,course,gdate,schname,gsdate))
            cur2.execute("INSERT INTO work(username, place1,design ,duration ,descr,place2,design1 ,duration1,descri)VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)", (uname,place1,design ,duration ,descr,place2,design1 ,duration1,descri))
            cur3.execute("INSERT INTO skills(username ,skill1,skill2,skill3,skill4,skill5) VALUES (%s,%s,%s,%s,%s,%s)",(uname,skill1,skill2,skill3,skill4,skill5))
            cur4.execute("INSERT INTO areas(username ,aeo1,aeo2,aeo3) VALUES (%s,%s,%s,%s)",(uname ,aeo1,aeo2,aeo3))
            # myq="""INSERT INTO areas(username ,aeo) VALUES (%s,%s)"""
            # records = [(uname,aoe1),
            #              (uname,aoe2),
            #              (uname,aoe3)]
            # cur4.executemany(myq, records)
            mysql.connection.commit()
            cur.close()
            cur1.close()
            cur2.close()
            cur3.close()
            cur4.close()
        return redirect(url_for('slogin'))
    else:
        return render_template('studentregister.html')
    return render_template('studentregister.html')
                

@app.route('/slogin',methods =['GET', 'POST'])
def slogin():
    if request.method == "POST":
        details = request.form
        uname = details['username']
        password = details['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM login")
        data = cur.fetchall()
        return render_template('loginsub.html', n=uname,p=password,login=data)
    return render_template('studentsignin.html')
    

@app.route('/slogin1')
def slogin1(id1):
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
    return render_template('test.html')
    #return render_template('signin1.html')
    
@app.route('/sprofile/<string:id1>',methods=['GET','POST'])
def sprofile(id1):
    if request.method == "GET":
        cur=mysql.connection.cursor()
        cur1=mysql.connection.cursor()
        cur2=mysql.connection.cursor()
        cur3=mysql.connection.cursor()
        cur4=mysql.connection.cursor()
        cur.execute("SELECT * from profile where username =%s",[id1])
        cur1.execute("SELECT * from info where username =%s",[id1])
        cur2.execute("SELECT * from work where username =%s",[id1])
        cur3.execute("SELECT * from skills where username =%s",[id1])
        cur4.execute("SELECT * from areas where username =%s",[id1])
        data = cur.fetchone()
        d=cur1.fetchone()
        e=cur2.fetchone()
        f=cur3.fetchone()
        g=cur4.fetchone()
    return render_template('studentprofile.html',data1=data,data2=d,data3=e,data4=f,data5=g)


@app.route('/searchf',methods=['GET','POST'])
def searchf():
    if request.method == "POST":
        details = request.form
        uname = details['nu']
        cur=mysql.connection.cursor()
        cur.execute("SELECT * from f_profile where proname =%s",[uname])
        data=cur.fetchone()
        return render_template('extra.html',n=data)
    return render_template('sample.html')


@app.route('/searchd',methods=['GET','POST'])
def searchd():
    if request.method == "POST":
        details = request.form
        uname = details['nu']
        cur=mysql.connection.cursor()
        cur.execute("SELECT * from f_profile where designation =%s",[uname])
        data=cur.fetchone()
        return render_template('extra.html',n=data)
    return render_template('sample.html')

@app.route('/searchexp',methods=['GET','POST'])
def searchexp():
    if request.method == "POST":
        details = request.form
        uname = details['nu']
        cur=mysql.connection.cursor()
        cur.execute("SELECT * from f_profile where years =%s",[uname])
        data=cur.fetchone()
        return render_template('extra.html',n=data)
    return render_template('sample.html')

@app.route('/searchaoe',methods=['GET','POST'])
def searchaoe():
    if request.method == "POST":
        details = request.form
        uname = details['nu']
        cur=mysql.connection.cursor()
        cur.execute("SELECT * from f_profile where f_username in(SELECT f_username from rearea where re1 = %s ",[uname])
        data=cur.fetchone()
        return render_template('extra.html',n=data)
    return render_template('sample.html')




#STUDENT PART END

#FACULTY PART

@app.route('/fregister', methods=['GET', 'POST'])
def fregister():
    if request.method == "POST":
        details = request.form
        f_username = details['f_username']
        f_password = details['f_password']
        cpass = details['cpassword']
        proname=details['proname']
        about =details['about']
        qualification=details['qualification'] 
        designation=details['designation']
        dob =details['dob']
        phone =details['phone']
        email =details['email']
        years=details['years']
        avail=details['avail']
        link=details['link']
        recess=details['recess']
        office=details['office']
        uni1 = details['uni1']
        qual1=details['qual1']
        period1=details['period1']
        uni2 = details['uni2']
        qual2=details['qual2']
        period2=details['period2']
        uni3 = details['uni3']
        qual3=details['qual3']
        period3=details['period3']
        skill1 = details['skill1']
        skill2 = details['skill2']
        skill3 = details['skill3']
        skill4 = details['skill4']
        skill5 = details['skill5']
        re1=details['re1']
        re2=details['re2']
        re3=details['re3']
        cur=mysql.connection.cursor()
        cur1 = mysql.connection.cursor()
        cur2 = mysql.connection.cursor()
        cur3 = mysql.connection.cursor()
        cur4 = mysql.connection.cursor()
        cur5=mysql.connection.cursor()
        if f_password == cpass:
            cur.execute("INSERT INTO flogin(f_username, f_password) VALUES (%s, %s)", (f_username, f_password))
            cur5.execute("INSERT INTO f_profile(proname , f_username ,about , qualification ,designation ,dob ,phone ,email , years ,avail ,link) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s,%s,%s)", (proname , f_username ,about , qualification ,designation ,dob ,phone ,email , years ,avail ,link))
            cur1.execute("INSERT INTO timings(f_username , r_hours,o_hours) VALUES(%s,%s,%s)",(f_username , recess,office))
            cur2.execute("INSERT INTO education(f_username ,uni1 ,qual1 ,period1 ,uni2,qual2 ,period2 ,uni3 ,qual3,period3) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s,%s)",(f_username ,uni1 ,qual1 ,period1 ,uni2,qual2 ,period2 ,uni3 ,qual3,period3))
            cur3.execute("INSERT INTO fskills(f_username ,skill1,skill2,skill3,skill4,skill5) VALUES (%s,%s,%s,%s,%s,%s)",(f_username,skill1,skill2,skill3,skill4,skill5))
            cur4.execute("INSERT INTO rearea(f_username ,re1,re2,re3) VALUES (%s,%s,%s,%s)",(f_username ,re1,re2,re3))
            # myq="""INSERT INTO areas(username ,aeo) VALUES (%s,%s)"""
            # records = [(uname,aoe1),
            #              (uname,aoe2),
            #              (uname,aoe3)]
            # cur4.executemany(myq, records)
            mysql.connection.commit()
            cur.close()
            cur1.close()
            cur2.close()
            cur3.close()
            cur4.close()
            cur5.close()
            return redirect(url_for('flogin'))
        else:
           return render_template('facultyregister.html')
    return render_template('facultyregister.html')

@app.route('/flogin',methods =['GET', 'POST'])
def flogin():
    if request.method == "POST":
        details = request.form
        uname = details['username']
        password = details['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM flogin")
        data = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return render_template('loginsub.html', n = uname,p=password,login=data)
    return render_template('facultysignin.html')
    

@app.route('/flogin1')
def flogin1(id1):
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
    return render_template('test.html')
    #return render_template('signin1.html')
    

@app.route('/fprofile/<string:id1>',methods=['GET','POST'])
def fprofile(id1):
    if request.method == "GET":
        cur=mysql.connection.cursor()
        cur.execute("SELECT * from f_profile where f_username =%s",[id1])
        data = cur.fetchone()
        mysql.connection.commit()
        cur.close()
    return render_template('studentprofile.html',data1=data)

@app.route('/updatefskill',methods =['GET', 'POST'])
def updatefskill():
    if request.method == "POST":
        details = request.form
        uname = details['username']
        skill1= details['skill1']
        skill2= details['skill2']
        skill3= details['skill3']
        skill4= details['skill4']
        skill5= details['skill5']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE fskills SET skill1=%s, skill2=%s, skill3=%s, skill4=%s,skill5=%s WHERE username=%s ", (skill1, skill2, skill3, skill4,skill5,uname))
        mysql.connection.commit()
        cur.close()
        
    return render_template('skills.html')

@app.route('/updatefaoe',methods =['GET', 'POST'])
def updatefaoe():
    if request.method == "POST":
        details = request.form
        uname = details['username']
        re1= details['aoe1']
        re2= details['aoe2']
        re3= details['aoe3']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE rearea SET re1=%s, re2=%s, re3=%s WHERE username=%s ", (re1, re2, re3,uname))
        mysql.connection.commit()
        cur.close()
        return 'Done'
    return render_template('areas.html')

#FACULTY PART END


#COMMON PART

@app.route('/message/<string:id1>',methods =['GET', 'POST'])
def message(id1):
    if request.method == "POST":
        details = request.form
        to = details['to']
        from1= id1
        message = details['message']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO message(message,to1,from1) VALUES (%s, %s,%s)", (message,to,from1))
        mysql.connection.commit()
        cur.close()
        return 
    return render_template('messages.html')

@app.route('/updateskill',methods =['GET', 'POST'])
def updateskill():
    if request.method == "POST":
        details = request.form
        uname = details['username']
        skill1= details['skill1']
        skill2= details['skill2']
        skill3= details['skill3']
        skill4= details['skill4']
        skill5= details['skill5']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE skills SET skill1=%s, skill2=%s, skill3=%s, skill4=%s,skill5=%s WHERE username=%s ", (skill1, skill2, skill3, skill4,skill5,uname))
        mysql.connection.commit()
        cur.close()
        
    return render_template('skills.html')

@app.route('/updateaoe',methods =['GET', 'POST'])
def updateaoe():
    if request.method == "POST":
        details = request.form
        uname = details['username']
        aeo1= details['aeo1']
        aeo2= details['aeo2']
        aeo3= details['aeo3']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE areas SET aeo1=%s, aeo2=%s, aeo3=%s WHERE username=%s ", (aeo1, aeo2, aeo3,uname))
        mysql.connection.commit()
        cur.close()
        return 'Done'
    return render_template('skills.html')

@app.route('/inbox/<string:id1>',methods =['GET', 'POST'])
def inbox(id1):
    if request.method == "GET":
        cur=mysql.connection.cursor()
        cur.execute("SELECT * from message where to1 =%s",[id1])
        data = cur.fetchall()
        mysql.connection.commit()
        cur.close()
    return render_template('inbox.html',data1=data)

@app.route('/reply/<string:id1>',methods =['GET', 'POST'])
def reply(id1):
    if request.method == "POST":
        details = request.form
        to = id1
        from1= details['from']
        message = details['message']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO message(message,to1,from1) VALUES (%s, %s,%s)", (message,to,from1))
        mysql.connection.commit()
        cur.close()
    return render_template('messages.html')


#COMMON PART

if __name__ == '__main__':
    app.run(debug = True )