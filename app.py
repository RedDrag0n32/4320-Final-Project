from flask import Flask, render_template, request, url_for, flash, redirect, abort
from authenticate import *
from Reserve import *

app = Flask(__name__)
app.config["DEBUG"] = True

app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    
    return render_template('index.html',)

@app.route("/reservations", methods = ['GET', 'POST'])
def reservations():
    reserved_seats = read_reserved_seats('reservations.txt')
    seat_array = create_seat_array(reserved_seats)
    if(request.method == "POST"):
        FirstName = request.form['Fname']
        LastName = request.form['Lname']
        Seatrow = request.form['Seatr']
        Seat = request.form['Seatc']
        # reserved_seats = read_reserved_seats('reservations.txt')
        # seat_array = create_seat_array(reserved_seats)

        if(FirstName == "Enter Text..."):
            flash("A first name must be entered!")
        elif(LastName == "Enter Text..."):
            flash("A first name must be entered!")
        elif(Seatrow == ""):
            flash("A seat row must be entered!")
        elif(Seat == ""):
            flash("A seat column must be entered!")
        else:
            #return render_template("reservations.html", seat_array=seat_array, total_sales=total_sales )
            #cost_matrix = get_cost_matrix()
            #total_sales = calculate_total_sales(reserved_seats, cost_matrix)
            message = Userinput(FirstName, LastName, Seatrow, Seat)
            reserved_seats = read_reserved_seats('reservations.txt')
            seat_array = create_seat_array(reserved_seats)
        return render_template('reservations.html', seat_array=seat_array, message = message)

    return render_template('reservations.html', seat_array=seat_array)
    
    #return render_template("reservations.html")

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
            reserved_seats = read_reserved_seats('reservations.txt')
            seat_array = create_seat_array(reserved_seats)
            cost_matrix = get_cost_matrix()
            total_sales = calculate_total_sales(reserved_seats, cost_matrix)
            return render_template("admin.html", seat_array=seat_array, total_sales=total_sales,)


    return render_template("admin.html")

app.run(debug=True, host='0.0.0.0')