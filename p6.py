from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('openlab.html')

@app.route('/result', methods=['GET', 'POST'])
def signup2():
    if request.method == 'POST':
        details = request.form
        name=details['cusname']
        id2=details['id']
        f = int(details['prev'])
        l = int(details['current'])
        amount=0
        d=l-f
        if d<200:
            amount = d*0.5
        elif d>200 and d<301:
            amount = 200*0.5+ (d-200)*0.75
        elif d>300 and d<501:   
            amount = 200*0.5+ 100*0.75+(d-300)*1
        else:
            amount=400*1+(d-400)*2
    return render_template('next.html',name=name,id1=id2,val=amount)

if __name__ == '__main__':
   app.run(debug = True)


      
