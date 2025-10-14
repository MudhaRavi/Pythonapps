# from unicodedata import digit
#
# password = input("Enter your password: ")
# result = {}
# if len(password) >= 8:
#     result["length"]=True
# else:
#     result["length"] = False
#
# digit = False
# for char in password:
#     if char.isdigit():
#         digit = True
# result["digits"] = digit
#
# uppercase = False
# for char in password:
#     if char.isupper():
#         uppercase = True
# result["upper"]= uppercase
#
# print(result)
#
# if all(result.values()):
#     print("Strong password")
# else:
#     print("Weak password")
#
#
#
# # Percentage calculator
# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#     percentage = value/total_value * 100
#     print(f"That is {percentage}%")
#
# except ValueError and ZeroDivisionError:
#     if  ValueError:
#         print("Total value cannot be zero. Run the program again.")
#     elif ZeroDivisionError:
#         print("You need to enter a number.Run the program again.")
#
#
#
#

#
# # Define a function named strength that takes one parameter, password
# def strength(password):
#     # Create an empty dictionary to store the strength attributes
#     result = {}
#
#     # Check the length of the password
#     if len(password) >= 8:
#         result["length"] = True
#     else:
#         result["length"] = False
#
#     # Check if the password contains a digit and an uppercase letter
#     digit = False
#     uppercase = False
#
#     # Iterate over each character in the password
#     for i in password:
#         # Check if the character is a digit
#         if i.isdigit():
#             digit = True
#         # Check if the character is an uppercase letter
#         if i.isupper():
#             uppercase = True
#
#     # Store the results in the dictionary
#     result["digits"] = digit
#     result["upper-case"] = uppercase
#
#     # Check if all the strength attributes are True
#     if all(result.values()):
#         # Return "Strong Password" if all attributes are True
#         return "Strong Password"
#     else:
#         # Return "Weak Password" if any attribute is False
#         return "Weak Password"



# def average(numbers):
#     total = sum(numbers)
#     count = len(numbers)
#     return total / count
#
# average([10, 20, 30,40,50])  # Example usage


def speed(distance, time):
    return distance / time


print(speed( 300,5))