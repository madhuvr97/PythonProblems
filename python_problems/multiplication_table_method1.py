def print_multiplication_table():
    while True:
        try:
            num = int(input("Enter the number for which you want multiplication table to be printed: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")

print_multiplication_table()
