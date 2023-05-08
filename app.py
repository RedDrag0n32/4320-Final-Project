from flask import Flask, render_template, request, url_for, flash, redirect, abort
from authenticate import *

app = Flask(__name__)
app.config["DEBUG"] = True

app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    
    return render_template('index.html',)

@app.route("/reservations", methods = ['GET', 'POST'])
def reservations():
    if(request.method == "POST"):
        FirstName = request.form['Fname']
        LastName = request.form['Lname']
        Seatrow = request.form['Seatr']
        Seat = request.form['Seatc']

        if(FirstName == "Enter Text..."):
            flash("A first name must be entered!")
        elif(LastName == "Enter Text..."):
            flash("A first name must be entered!")
        elif(Seatrow == "Enter number from 1 to 12"):
            flash("A seat row must be entered!")
        elif(Seat == "Enter number from 1 to 4"):
            flash("A seat column must be entered!")
        else:
            return render_template("reservations.html")
    
    return render_template("reservations.html")

@app.route("/admin", methods = ['GET', 'POST'])
def admin():

    if(request.method == "POST"):
        user_name = request.form['userName']
        password = request.form['password']

        if(user_name == "Enter Text..."):
            flash("A user name must be entered!")
        elif(password == "Enter Text..."):
            flash("A password must be entered!")
        elif(not authenticate(user_name, password)):
            flash("Incorrect username or password")
        else:
            return render_template("admin.html")


    return render_template("admin.html")

app.run()