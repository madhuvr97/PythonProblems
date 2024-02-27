class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful.")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Balance: {self.balance}")


if __name__ == "__main__":
    try:
        account_number = input("Enter your account number: ")
        if not account_number.isdigit() or len(account_number) != 15:
            raise ValueError("Account number must be a 15-digit numeric value.")

        account_holder_name = input("Enter your sweet name: ")
        if not account_holder_name.isalpha():
            raise ValueError("Account holder name must contain only alphabetic characters.")

        balance = int(input("Enter the balance amount in your account: "))
        if balance < 0:
            raise ValueError("Balance amount cannot be a negative number.")

        account = BankAccount(account_number, account_holder_name, balance)
        deposit_amount = int(input("Enter the deposit amount: "))
        account.deposit(deposit_amount)

        withdrawal_amount = int(input("Enter the withdrawal amount: "))
        account.withdraw(withdrawal_amount)

        account.display_details()

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)
