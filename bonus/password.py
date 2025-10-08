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


