from unicodedata import digit

password = input("Enter your password: ")
result = {}
if len(password) >= 8:
    result["length"]=True
else:
    result["length"] = False

digit = False
for char in password:
    if char.isdigit():
        digit = True
result["digits"] = digit

uppercase = False
for char in password:
    if char.isupper():
        uppercase = True
result["upper"]= uppercase

print(result)

if all(result.values()):
    print("Strong password")
else:
    print("Weak password")



# Percentage calculator
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = value/total_value * 100
    print(f"That is {percentage}%")

except ValueError and ZeroDivisionError:
    if  ValueError:
        print("Total value cannot be zero. Run the program again.")
    elif ZeroDivisionError:
        print("You need to enter a number.Run the program again.")




