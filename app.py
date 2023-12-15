## 1. Flak App Routing

from flask import Flask,render_template,request,redirect,url_for

## Create a Simple Flask Application

app=Flask(__name__)    ###name-> Entry points

@app.route("/",methods=["GET"])
def welcome():
    return "Welcome to Ram Channel"


@app.route("/index",methods=["GET"])
def index():
    return "Welcome to Index Page"

##Variable Rule

@app.route('/success/<int:score>')
def success (score):
    return "The Person has passed and the score is :"+ str(score)


@app.route('/fail/<int:score>')
def fail (score):
    return "The Person has failed and the score is :"+ str(score)


@app.route('/form',methods=["GET","POST"])
def form():
    if request.method=='GET':
        return render_template('form.html')
    else:

        maths=float(request.form['maths'])
        science=float(request.form['science'])
        Geopolitics=float(request.form['Geopolitics'])

        average_marks=(maths+science+Geopolitics)/3

        result=" "
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks))

        return render_template('form.html',score=average_marks)





if __name__=="__main__":
    app.run(debug=True)
