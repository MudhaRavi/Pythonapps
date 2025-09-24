password = input("Enter your password: ")

while password != "pass123":
    print("Incorrect password, try again.")
    password = input("Enter your password: ")
print("Access granted.")