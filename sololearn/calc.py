#!/usr/bin/python3
while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("enter 'quit' to to end the programm")
    user_input = input(": ")

    if user_input == "quit":
        break
    if user_input == "add":
       	num1 = float(input("Enter a number: "))
       	num2 = float(input("Enter another number:"))
       	result = str(num1 + num2)
    if user_input == "subtract":
        num1 = float(input("Enter a number: "))
       	num2 = float(input("Enter another number:"))
       	result = str(num1 - num2)
    if user_input == "multiply":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number:"))
        result = str(num1 * num2)
    if user_input == "divide":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number:"))
        result = str(num1 / num2)
    else:
        print("Unknown input")
    print("The answer is " + result)
