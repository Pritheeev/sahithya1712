from flask import Flask
from flask_mysqldb import MySQL


app=Flask(__name__)

app.config['MYSQL_USER']='sql12326774'
app.config['MYSQL_PASSWORD']='fQr3hGyArQ'
app.config['MYSQL_HOST']='sql12.freemysqlhosting.net'
app.config['MYSQL_DB']='sql12326774'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)

@app.route('/')
def index():
    cur=mysql.connection.cursor()
    return 'Done!'

if __name__ == '__main__':
    app.run(debug = True )