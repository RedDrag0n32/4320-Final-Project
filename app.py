from flask import Flask, render_template, request, url_for, flash, redirect, abort
from authenticate import *
from Reserve import *

app = Flask(__name__)
app.config["DEBUG"] = True

app.config['SECRET_KEY'] = 'your secret key'



@app.route("/", methods = ['GET', 'POST'])
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

def reservation_page():
    reserved_seats = read_reserved_seats('reservations.txt')
    seat_array = create_seat_array(reserved_seats)
    return render_template('reservation.html', seat_array=seat_array)

@app.route('/reservation/')
def reservation_page():
    reserved_seats = read_reserved_seats('reservations.txt')
    seat_array = create_seat_array(reserved_seats)
    cost_matrix = get_cost_matrix()
    total_sales = calculate_total_sales(reserved_seats, cost_matrix)
    return render_template('reservation.html', seat_array=seat_array, total_sales=total_sales)

app.run()