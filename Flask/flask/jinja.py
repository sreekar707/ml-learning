

from flask import Flask,render_template,request,redirect,url_for

###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the website </H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    return render_template('results.html',results=score)

## Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    exp={'score':score,"res":res}

    return render_template('results1.html',results=exp)

## if confition
@app.route('/successif/<int:score>')
def successif(score):

    return render_template('results.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('results.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresults.html')
    return redirect(url_for('successres',score=total_score))
            
        




if __name__=="__main__":
    app.run(debug=True)