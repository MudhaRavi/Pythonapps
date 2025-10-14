# def get_average():
#     with open("files/data.txt",'r') as file:
#         data = file.readlines()
#         values = data[1:] # Skip the header line
#         values = [float(i) for i in values] # Convert strings to floats
#         average_local = sum(values) / len(values)
#
#     return average_local
#
#
# average = get_average()
# print(f"The average is: {average}")


#
# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     maximum = max(grades)
#     minimum = min(grades)
#     message = f"Max = {maximum}, Min = {minimum}"
#     return message


def get_maximum():
    celsius_local = [14, 15.1, 12.3]
    maximum = max(celsius_local)
    return maximum


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32

print(fahrenheit)