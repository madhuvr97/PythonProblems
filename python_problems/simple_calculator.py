def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        return "Cannot divide by 0"
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        if choice not in (1,2,3,4):
            raise ValueError("Please enter your choice correctly.")
        else:
            try:
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))
            except:
                raise ValueError("Please enter integers or floats only")

        if choice == 1:
            print(f"{x} + {y} = {addition(x,y)}")
            break

        elif choice == 2:
            print(f"{x} - {y} = {subtraction(x, y)}")
            break

        elif choice == 3:
            print(f"{x} x {y} = {multiplication(x, y)}")
            break

        elif choice == 4:
            result = division(x, y)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{x} / {y} = {result}")
            break
    except ValueError as ve:
        print("Invalid input: ", str(ve))
    except Exception as e:
        print("An unknown error occurred: ", str(e))
