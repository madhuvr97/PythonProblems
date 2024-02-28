def check_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return "Leap year"
    else:
        return "Not a leap year"

try:
    year = int(input("Enter the year: "))
    if year <= 0:
        print("Input year cannot be negative or zero.")
    else:
        leap_year_check = check_leap_year(year)
        print(f"The year {year} is {leap_year_check}")
except ValueError as ve:
    print("Invalid input: ", str(ve))
