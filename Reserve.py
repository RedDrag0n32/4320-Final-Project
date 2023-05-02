import random
import string

# Save the user inputs to a file
def save_to_file(file_name, first_name, seat_row, seat_column, 
reservation_code):
    with open(file_name, 'a') as f:
        
f.write(f'{first_name},{seat_row},{seat_column},{reservation_code}\n')

def Userinput(length=15):
    FirstName = input("Enter First name:  ")
    LastName = input("Enter Last name:  ")
    Seatrow = int(input("Enter row choice: "))
    Seat = int(input("Enter seat choice: "))

    # Generate a random string 
    random_str = ''.join(random.choices(string.ascii_uppercase + 
string.digits, k=length -2 ))

    # Create a reservation code using the first letter, the last letter, 
and the random string
    reservation_code = 
f"{FirstName[0].upper()}{LastName[-1].upper()}{random_str}"

    print(f"Congratulations {FirstName}, your seat row is {Seatrow}, and 
the seat number is seat number {Seat}, here is your reservation code = 
{reservation_code}")


     # Save the input and reservation code to a file
    save_to_file("reservations.txt", FirstName, Seatrow, Seat, 
reservation_code)


Userinput()


