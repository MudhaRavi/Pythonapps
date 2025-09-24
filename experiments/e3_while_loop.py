

# names = []
# while True:
#     name = input("what is your name: ").capitalize()
#     if name == "Exit":
#         break
#     names.append(name)
# print(f"Names: {names}")


#Write a program that uses a while loop to print numbers from 1 to 10.
# x = 1
# count = []
#
# while x <= 10:
#     count.append(x)
#     x = x + 1
# print(count)


# Sum of digits
# number = int(input("Enter a number: "))
# total = 0
#
# while number > 0:
#     digits = number % 10
#     total = total + digits
#     number = number // 10
# print(f"Sum of digits: {total}")


# random number guessing game
# import random
# number = random.randint(1, 10)
# guess = int(input("Guess: "))
# count = 0
# while number != guess:
#     print("Guess again.")
#     guess = int(input("Guess: "))
#     count =count + 1
# print(f'You guessed it! and the counter is :' , count)



#Reverse the number
# number = int(input("Enter a number: "))
#
# rev = 0
# while number > 0:
#     digit = number % 10
#     rev = rev * 10 + digit
#     number = number // 10
# print(f"Reversed Number: {rev}")


# Multiplication table
# number = int(input("enter the number "))
# i = 1
# while number > 0:
#     print(number * i)
#     i = i + 1
#     if i > 10:
#         break
# print("table of " , number)


