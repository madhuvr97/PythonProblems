while True:
    try:
        num = int(input("Enter the number for which you want multiplication table to be printed: "))
        break  # Break out of the loop if input is valid
    except ValueError:
        print("Please enter a valid integer.")

for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")