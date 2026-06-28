import math
import random
from datetime import datetime

history = {}

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    print("\n----- Smart Calculator -----")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculation")
    print("3. Generate Random Number")
    print("4. View History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            op = input("Enter operation (+,-,*,/): ")

            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = sub(a, b)
            elif op == "*":
                result = mul(a, b)
            elif op == "/":
                result = div(a, b)
            else:
                print("Invalid operation")
                continue

            print("Result:", result)
            history[str(datetime.now())] = result

        elif choice == "2":
            num = float(input("Enter a number: "))
            print("Square Root:", math.sqrt(num))
            history[str(datetime.now())] = math.sqrt(num)

        elif choice == "3":
            r = random.randint(1, 100)
            print("Random Number:", r)
            history[str(datetime.now())] = r

        elif choice == "4":
            print("\nHistory:")
            for key, value in history.items():
                print(key, ":", value)

        elif choice == "5":
            print("Program Ended.")
            break

        else:
            print("Invalid Choice.")

    except ValueError:
        print("Invalid Input.")

    except ZeroDivisionError:
        print("Division by zero is not allowed.")

    except Exception as e:
        print("Error:", e)
