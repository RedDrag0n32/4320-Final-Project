from flask import Flask, render_template, request, url_for, flash, redirect, abort
from authenticate import *

app = Flask(__name__)
app.config["DEBUG"] = True

app.config['SECRET_KEY'] = 'your secret key'



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