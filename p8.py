from flask import Flask, render_template

app=Flask(name)
@app.route('/<st>')
def valid(st):
   l=len(s)
   if(l==8):
       d=st[0:3]
       no=st[3:8]
       if(dep.isalpha() and no.isnumeric()):
           return 'Valid'
       else:
           return 'Invalid'
   elif(l==11):
       d = st[0:3]
       no = st[3:11]
       if (d.isalpha() and no.isnumeric()):
           return 'Valid'
       else:
           return 'inValid'
   else:
       return 'inValid'



if(name=='main'):
    app.run(debug=True,port=8080)