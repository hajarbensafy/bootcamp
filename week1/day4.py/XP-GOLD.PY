# Part I: BankAccount Class
class BankAccount:
    def __init__(self, balance=0, username="", password=""):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            print("Authentication successful.")
        else:
            print("Authentication failed.")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to deposit.")
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to withdraw.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


# Part II: MinimumBalanceAccount Class
class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimum_balance=0, username="", password=""):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to withdraw.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception("Withdrawal would go below the minimum balance.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


# Part IV: ATM Class
class ATM:
    def __init__(self, account_list, try_limit=2):
        if not all(isinstance(account, (BankAccount, MinimumBalanceAccount)) for account in account_list):
            raise Exception("account_list must contain only BankAccount or MinimumBalanceAccount instances.")
        if try_limit <= 0:
            print("Invalid try_limit. Setting to default value of 2.")
            try_limit = 2
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Log in")
            print("2. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def log_in(self, username, password):
        for account in self.account_list:
            account.authenticate(username, password)
            if account.authenticated:
                self.show_account_menu(account)
                return
        self.current_tries += 1
        if self.current_tries >= self.try_limit:
            print("Max tries reached. Shutting down.")
            exit()
        print("Invalid username or password. Please try again.")

    def show_account_menu(self, account):
        while True:
            print("\nAccount Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                try:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "2":
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")


