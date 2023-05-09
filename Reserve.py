import random
import string

# Save the user inputs to a file
def savefile(file_name, first_name, seat_row, seat_column, e_ticket_number):
    with open(file_name, 'a') as f:
        f.write(f'{first_name},{seat_row},{seat_column},{e_ticket_number}\n')


def Userinput(FirstName, LastName, Seatrow, Seat, length=15):
    # FirstName = input("Enter First name:  ")
    # LastName = input("Enter Last name:  ")
    # Seatrow = int(input("Enter row choice: "))
    # Seat = int(input("Enter seat choice: "))

    # Generate a random string 
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, 
k=length ))

    # Create a reservation code 
    e_ticket_number = f"{FirstName[0].upper()}{LastName[-1].upper()}{random_str}"

    # Save the input and reservation code to a file
    savefile("reservations.txt", FirstName, Seatrow, Seat, e_ticket_number)

    message = (f"Congratulations {FirstName}, your seat row is {Seatrow}, and the seat number is seat number {Seat}, here is your reservation code = {e_ticket_number}")

    return message




def create_seat_array(reserved_seats):
    seat_array = [['O' for _ in range(4)] for _ in range(12)]

    for seat in reserved_seats:
        row, column = seat
        if 0 <= row < 12 and 0 <= column < 4:
            seat_array[row][column] = 'X'

    return seat_array


def read_reserved_seats(file_path):
    reserved_seats = []
    with open(file_path, 'r') as file:
        for line in file:
            name, row, column, reservation_code = [x.strip() for x in line.strip().split(',')]
            reserved_seats.append((int(row), int(column)))
    return reserved_seats


def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

def calculate_total_sales(reserved_seats, cost_matrix):
    total_sales = 0
    for row, column in reserved_seats:
        if row < len(cost_matrix) and column < len(cost_matrix[0]):
            total_sales += cost_matrix[row][column]
    return total_sales


#Userinput()


