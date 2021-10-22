def factorial(number):
    if number < 0:
        return 0
    elif number == 1 or number == 0:
        return number
    return number * factorial(number -1)

print(factorial(5))
