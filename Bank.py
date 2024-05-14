import uuid


class Bank:
    def __init__(self, account_holder_name, ifsc_code, balance, branch, account_number):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.ifsc_code = ifsc_code
        self.balance = balance
        self.branch = branch

    def credit_amount(self, amount):
        if amount < 0:
            print("Please Enter the Valid Amount and Try Again!!")
            return
        self.balance = self.balance + amount
        print(f"Balance Credited. {amount}"
              f"Total Available Balance: {self.balance}")

    def debit_amount(self, amount):
        if amount > self.balance:
            print(f"Insufficient Amount!!\n"
                  f"Available Balance: {self.balance}")
            return
        elif amount < 0:
            print("Invalid Amount Entered!!! Please Enter the valid amount")
            return
        else:
            self.balance = self.balance - amount
            print(f"Balance Debited. {amount}"
                  f"Total Available Balance: {self.balance}")

    def view_balance(self):
        print("Available Balance: ", self.balance)

    def view_account_details(self):
        print(f"Account Number: {self.account_number}\n"
              f"Account Holder Name: {self.account_holder_name}\n"
              f"Balance: {self.balance}\n"
              f"IFSC CODE: {self.ifsc_code}\n"
              f"Branch Name: {self.branch}")


def main():
    print("Welcome To the Bank\n")
    print("Enter the Bank Details\n")

    account_number = uuid.uuid4()
    account_holder_name = input("Please Enter the holder name: ")
    ifsc_code = "110BFS001"
    branch = "abc branch"
    balance = float(input("Please Enter the Initial Balance: "))

    bank_obj = Bank(account_holder_name, ifsc_code, balance, branch, account_number)
    while True:
        print(f"1. Credit Amount\n"
              f"2. Debit Amount\n"
              f"3. View Bank Details\n"
              f"4. View Bank Balance\n"
              f"5. EXIT")

        choice = int(input("Please Choose: "))

        if choice == 1:
            amount = float(input("Please Enter the Amount:: "))
            bank_obj.credit_amount(amount)
        elif choice == 2:
            amount = float(input("Please Enter the Amount:: "))
            bank_obj.debit_amount(amount)
        elif choice == 3:
            bank_obj.view_account_details()
        elif choice == 4:
            bank_obj.view_balance()
        elif choice == 5:
            break
        else:
            print("Invalid Choice!!!!!!!!")


if __name__ == '__main__':
    main()
