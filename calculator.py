#!/usr/bin/env python3

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print(" Choose a function: \n 1) Add \n 2) Subtract \n 3) Multiply \n 4) Divide ")

while True:
    selection = input(" Select your function(1/2/3/4): ")
    if selection in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if selection == '1':
            print(num1, '+' , num2, '=', add(num1, num2))

        elif selection == '2':
            print(num1, '-' , num2, '=', subtract(num1, num2))

        elif selection == '3':
            print(num1, '*' , num2, '=', multiply(num1, num2))

        elif selection == '4':
            print(num1, '/' , num2, '=', divide(num1, num2))
        break
    else:
        print("Invalid input")



