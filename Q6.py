import random
import math

try:
    numbers = set()

    while len(numbers) < 10:
        num = int(input("Enter a number: "))
        numbers.add(num)

    print("Set:", numbers)

    tup = tuple(numbers)
    print("Tuple:", tup)

    print("3 Random Numbers:")
    print(random.sample(tup, 3))

    total = sum(tup)
    print("Square Root of Sum:", math.sqrt(total))

except ValueError:
    print("Please enter valid integers.")

except Exception as e:
    print("Error:", e)
