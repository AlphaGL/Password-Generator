import random

alphabets = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","W","w","X","x","Y","y","Z","z"]
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*']

def generate_password():
    print("Welcome to the PyPassword Generator!")
    nr_alphabets = int(input("How many letters would you like in your password?\n"))
    nr_numbers = int(input("How many numbers would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like in your password?\n"))

    password_list = []

    for char in range(1, nr_alphabets + 1):
        password_list.append(random.choice(alphabets))

    for char in range(1, nr_numbers + 1):
        password_list.append(random.choice(numbers))

    for char in range(1, nr_symbols + 1):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    
    password = "".join(password_list)
    
    print(f"Your password is: {password}")

def new_password():
    while True:
        rebuild = input("Do you want to generate a new password? 'Y' or 'N' \n").capitalize()
        if rebuild == "Y":
            generate_password()
        elif rebuild == "N":
            print("Goodbye!")
            break
        else:
            print("Invalid input! Please enter 'Y' or 'N'.")

# Generate the first password
generate_password()

# Ask for new password
new_password()
