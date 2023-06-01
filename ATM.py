class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
                Enter 1 to Create Pin
                Enter 2 to Deposit
                Enter 3 to check balance
                Enter 4 to Withdraw
                Enter 5 to Exit        
            """)

            if user_input == "1":
                self.Create_Pin()
            elif user_input == "2":
                self.Deposit()
            elif user_input == "3":
                self.Check_balance()
            elif user_input == "4":
                self.Withdraw()
            elif user_input == "5":
                print("Thank you for using our Bank")
                break

    def Create_Pin(self):
        self.pin = input("Enter your pin: ")

    def Deposit(self):
        p = input("Enter your pin: ")
        if p == self.pin:
            amount = int(input("Enter the amount: "))
            self.balance = self.balance + amount
            print("Deposit Successful")
        else:
            print("Wrong Pin")

    def Check_balance(self):
        p = input("Enter your pin: ")
        if p == self.pin:
            print(self.balance)
        else:
            print("Wrong Pin")

    def Withdraw(self):
        p = input("Enter your pin: ")
        if p == self.pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Withdrawal Successful")
            else:
                print("Insufficient Balance")
        else:
            print("Wrong Pin")


sbi = Atm()
