import random
import string

# Save the user inputs to a file
def savefile(file_name, first_name, seat_row, seat_column, e_ticket_number):
    with open(file_name, 'a') as f:
        f.write(f'{first_name},{seat_row},{seat_column},{e_ticket_number}\n')


def Userinput(length=15):
    FirstName = input("Enter First name:  ")
    LastName = input("Enter Last name:  ")
    Seatrow = int(input("Enter row choice: "))
    Seat = int(input("Enter seat choice: "))

    # Generate a random string 
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, 
k=length ))

    # Create a reservation code 
    e_ticket_number = f"{FirstName[0].upper()}{LastName[-1].upper()}{random_str}"

    print(f"Congratulations {FirstName}, your seat row is {Seatrow}, and the seat number is seat number {Seat}, here is your reservation code = {e_ticket_number}")


     # Save the input and reservation code to a file
    savefile("reservations.txt", FirstName, Seatrow, Seat, e_ticket_number)


Userinput()


