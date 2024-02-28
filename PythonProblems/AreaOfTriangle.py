import math

def AreaOfTriangle(s1, s2, s3):
    """
    Calculate the area of a triangle given the lengths of its three sides.

    Parameters:
    - s1, s2, s3: Positive integers representing the lengths of the sides of the triangle.

    Returns:
    - The area of the triangle if it can be formed with the provided side lengths, 0 otherwise.
    """
    # Check if the side lengths can form a triangle
    if s1 <= 0 or s2 <= 0 or s3 <= 0 or (s1 + s2 <= s3) or (s1 + s3 <= s2) or (s2 + s3 <= s1):
        raise ValueError("Invalid side lengths. Triangle cannot be formed.")

    # Calculate the semi-perimeter
    s = (s1 + s2 + s3) / 2

    # Calculate the area using Heron's formula
    result = round(math.sqrt(s * (s - s1) * (s - s2) * (s - s3)), 2)
    return result


try:
    s1 = int(input("Enter the length of side1: "))
    s2 = int(input("Enter the length of side2: "))
    s3 = int(input("Enter the length of side3: "))
    calculate_area = AreaOfTriangle(s1, s2, s3)
    print("The area of the triangle is", calculate_area)
except ValueError as ve:
    print("Invalid input:", str(ve))
except Exception as e:
    print("An error occurred:", str(e))
