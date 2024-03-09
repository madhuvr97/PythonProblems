def analyze_number(num):
    if num > 0 and num % 2 == 0:
        return "positive and even"
    elif num > 0 and num % 2 == 1:
        return "positive and odd"
    elif num < 0:
        return "negative"
    else:
        return "not a valid integer"


try:
    num = int(input("Enter a number: "))
    result = analyze_number(num)
    print(f"The number you entered is {result}.")
except ValueError as ve:
    print("Enter valid input: ", str(ve))
