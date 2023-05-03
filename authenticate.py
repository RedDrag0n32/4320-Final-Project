
def authenticate(user_name, password):


    with open("passcodes.txt", "r") as file:

        # lines = file.readlines()
        # data.append(lines)

        while True:
            line = file.readline().strip()
            #split the data
            elements = line.split(", ")
            
            if(user_name in elements and password in elements):
                return True
            
            if not line:
                return False
        
    


# def main():
#     data = authenticate("admin2", "98765")

#     print(data)

# main()