import math
def sqrt_number(num):
    if num < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    result = round(math.sqrt(num),2)
    return result
try:
    num = int(input("Enter a non-negative number for which you want to find the square root: "))
    square_root_of_number = sqrt_number(num)
    print("Square root of", num, "is", square_root_of_number)
except ValueError as ve:
    print("Invalid input: ", str(ve))
except Exception as e:
    print("An unknown error occurred", str(e))