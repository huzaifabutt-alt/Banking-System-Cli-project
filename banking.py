import os
import json

class BankAccount:
    def __init__(self, dollars, cents, password):
        if dollars < 0 or cents < 0:
            raise ValueError("Dollars and cents must be non-negative.")
        self.dollars = dollars
        self.cents = cents
        self.password = password

    def withdraw(self, dollar_amount, cent_amount):
        if dollar_amount < 0 or cent_amount < 0:
            raise ValueError("Withdrawal amounts must be non-negative.")

        if dollar_amount > self.dollars or (dollar_amount == self.dollars and cent_amount > self.cents):
            raise ValueError("Insufficient funds.")

        # Handle cases where cents to be withdrawn exceed current cents
        if cent_amount > self.cents:
            self.dollars -= (dollar_amount + 1)
            self.cents = self.cents + 100 - cent_amount
        else:
            self.dollars -= dollar_amount
            self.cents -= cent_amount

        # Ensure dollars and cents remain non-negative
        if self.dollars < 0 or self.cents < 0:
            raise ValueError("Withdrawal results in negative balance.")

    def deposit(self, dollar_amount, cent_amount):
        if dollar_amount < 0 or cent_amount < 0:
            raise ValueError("Deposit amounts must be non-negative.")

        self.dollars += dollar_amount
        self.cents += cent_amount

        # Normalize cents to ensure it's less than 100
        if self.cents >= 100:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100

    def __str__(self):
        return f"Balance: {self.dollars} dollars, {self.cents} cents"

    def to_dict(self):
        return {"dollars": self.dollars, "cents": self.cents, "password": self.password}

    @staticmethod
    def from_dict(data):
        return BankAccount(data["dollars"], data["cents"], data["password"])

# Functions to handle file storage and account management
def load_accounts(filename="accounts.txt"):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as file:
        return json.load(file)

def save_accounts(accounts, filename="accounts.txt"):
    with open(filename, "w") as file:
        json.dump(accounts, file)

if __name__ == "__main__":
    accounts = load_accounts()

    while True:
        print("\nWelcome to the Banking System")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            os.system('cls')
            username = input("Enter your username: ")
            if username not in accounts:
                print("Account does not exist. Please create an account.")
                continue

            password = input("Enter your password: ")
            account_data = accounts[username]
            account = BankAccount.from_dict(account_data)

            if account.password != password:
                print("Incorrect password.")
                continue

            while True:
                os.system('cls')
                print("\nCurrent Account Balance:", account)
                print("Choose an operation:")
                print("1. Deposit Money")
                print("2. Withdraw Money")
                print("3. Transfer Money")
                print("4. Logout")

                operation = input("Enter your choice (1/2/3/4): ")

                if operation == "1":
                    os.system('cls')
                    print("\nCurrent Account Balance:", account)
                    dollar_amount = int(input("Enter dollars to deposit: "))
                    cent_amount = int(input("Enter cents to deposit: "))
                    account.deposit(dollar_amount, cent_amount)
                elif operation == "2":
                    os.system('cls')
                    print("\nCurrent Account Balance:", account)
                    dollar_amount = int(input("Enter dollars to withdraw: "))
                    cent_amount = int(input("Enter cents to withdraw: "))
                    try:
                        account.withdraw(dollar_amount, cent_amount)
                    except ValueError as e:
                        print("Error:", e)
                elif operation == "3":
                    os.system('cls')
                    print("\nCurrent Account Balance:", account)
                    recipient = input("Enter recipient username: ")
                    if recipient not in accounts:
                        print("Recipient account does not exist.")
                        continue

                    transfer_dollars = int(input("Enter dollars to transfer: "))
                    transfer_cents = int(input("Enter cents to transfer: "))

                    try:
                        account.withdraw(transfer_dollars, transfer_cents)
                        recipient_account_data = accounts[recipient]
                        recipient_account = BankAccount.from_dict(recipient_account_data)
                        recipient_account.deposit(transfer_dollars, transfer_cents)
                        accounts[recipient] = recipient_account.to_dict()
                        print("Transfer successful.")
                    except ValueError as e:
                        print("Error:", e)
                elif operation == "4":
                    os.system('cls')
                    accounts[username] = account.to_dict()
                    save_accounts(accounts)
                    print("Logged out.")
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "2":
            os.system('cls')
            username = input("Choose a username: ")
            if username in accounts:
                print("Username already exists. Please choose another.")
                continue

            password = input("Create a password: ")
            dollars = int(input("Enter initial dollars: "))
            cents = int(input("Enter initial cents: "))

            account = BankAccount(dollars, cents, password)
            accounts[username] = account.to_dict()
            save_accounts(accounts)
            print("Account created successfully.")
            os.system('cls')

        elif choice == "3":
            os.system('cls')
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")
