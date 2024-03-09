import cmath

def sqrt_number(num):
    if num.real < 0 and num.imag == 0:
        raise ValueError("Square root is not defined for negative real numbers.")
    result = cmath.sqrt(num)  # Using cmath.sqrt() for complex numbers
    return result

try:
    num_str = input("Enter a number for which you want to find the square root (in the format a+bj): ")
    num = complex(num_str)
    square_root_of_number = sqrt_number(num)
    rounded_square_root = round(square_root_of_number.real, 2) + round(square_root_of_number.imag, 2) * 1j
    print("Square root of", num, "is approximately", rounded_square_root)
except ValueError as ve:
    print("Invalid input:", str(ve))
except Exception as e:
    print("An unknown error occurred:", str(e))
