def generate_fibonacci_series(limit):
    fibonacci_series = []

    def fibonacci(n):
        #Base Case: In recursive functions, a base case is a condition that stops the recursion and provides a result without further recursive calls. Without a base case, the recursive function would continue to call itself indefinitely, leading to infinite recursion
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    for i in range(limit):
        fibonacci_series.append(fibonacci(i))

    return fibonacci_series


while True:
    try:
        limit = int(input("Enter the limit until which you want to print the Fibonacci series: "))
        if limit <= 0:
            print("Limit must be a positive integer.")
        else:
            fibonacci_list = generate_fibonacci_series(limit)
            print(f"fibonacci series up to limit {limit} is {fibonacci_list}")
            break
    except ValueError as ve:
        print("Invalid input: ", str(ve))
    except Exception as e:
        print("An unknown error occurred", str(e))
