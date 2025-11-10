#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

    pass

def hows_the_weather(temperature):
    if temperature<40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    if temperature>85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

    # your code here
    pass

def fizzbuzz(num):
    if num%5== 0 ==num%3:
        return "FizzBuzz"
    elif num%5==0:
        return "Buzz"
    elif num%3==0:
        return "Fizz"
    else:
        return num

    pass

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

    else:
        print("Invalid operation!")
        return None


    # your code here
    pass

