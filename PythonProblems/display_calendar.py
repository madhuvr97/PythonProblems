import calendar

def get_valid_year():
    while True:
        try:
            year = int(input("Enter the year: "))
            if year < 0:
                raise ValueError("Year cannot be negative")
            return year
        except ValueError:
            print("Invalid input. Please enter a valid year.")

def get_valid_month():
    while True:
        try:
            month = int(input("Enter the month (1-12): "))
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12")
            return month
        except ValueError:
            print("Invalid input. Please enter a valid month (1-12).")

def print_calendar(year, month):
    cal = calendar.month(year, month)
    print(f"Calendar for {calendar.month_name[month]} {year}:")
    print(cal)

if __name__ == "__main__":
    try:
        year = get_valid_year()
        month = get_valid_month()
        print_calendar(year, month)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print("An error occurred:", str(e))
