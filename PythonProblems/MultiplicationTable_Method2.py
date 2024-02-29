def get_integer_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please enter a valid integer.")

def print_multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")

def main():
    num = get_integer_input("Enter the number for which you want multiplication table to be printed: ")
    print_multiplication_table(num)

if __name__ == "__main__":
    main()

