from pathlib import Path

FILE_NAME = "bank.txt"
bank_file = Path(FILE_NAME)   # represents the file bank.txt
MIN_BALANCE = 500




def load_accounts():

    accounts = []

    if not bank_file.exists():      # no file yet, so no accounts
        return accounts

    text = bank_file.read_text()    # read the whole file as one string
    for line in text.splitlines():  # go through it line by line
        line = line.strip()
        if line != "":
            parts = line.split(",")
            acc_no = int(parts[0])
            name = parts[1]
            balance = int(parts[2])
            accounts.append([acc_no, name, balance])
    return accounts


def save_accounts(accounts):
    text = ""
    for acc in accounts:
        text = text + str(acc[0]) + "," + acc[1] + "," + str(acc[2]) + "\n"
    bank_file.write_text(text)      # write the whole string to the file


# ---------- HELPER FUNCTIONS ----------

def find_account(accounts, acc_no):
    for acc in accounts:
        if acc[0] == acc_no:
            return acc
    return None


def new_account_number(accounts):
    if len(accounts) == 0:
        return 1001
    return accounts[-1][0] + 1


def read_number(message):
    while True:
        text = input(message)
        if text.isdigit():
            return int(text)
        print("Invalid input. Please enter a whole number.")


def read_amount(message):
    while True:
        amount = read_number(message)
        if amount > 0:
            return amount
        print("Amount must be greater than 0.")


# ---------- BANK FUNCTIONS ----------

def create_account(accounts):
    name = input("Name: ").strip()
    if name == "" or "," in name:
        print("Invalid name. Account not created.")
        return
    deposit = read_amount("Opening deposit: ")
    if deposit < MIN_BALANCE:
        print("Opening deposit must be at least Rs.500. Account not created.")
        return
    acc_no = new_account_number(accounts)
    accounts.append([acc_no, name, deposit])
    save_accounts(accounts)
    print("Account created. A/C No:", acc_no, "| Balance:", deposit)


def deposit_money(accounts):
    acc_no = read_number("Account number: ")
    acc = find_account(accounts, acc_no)
    if acc is None:
        print("Account", acc_no, "not found.")
        return
    amount = read_amount("Deposit amount: ")
    acc[2] = acc[2] + amount
    save_accounts(accounts)
    print("Deposit successful. Balance:", acc[2])


def withdraw_money(accounts):
    acc_no = read_number("Account number: ")
    acc = find_account(accounts, acc_no)
    if acc is None:
        print("Account", acc_no, "not found.")
        return
    amount = read_amount("Withdraw amount: ")
    if acc[2] - amount < MIN_BALANCE:
        print("Withdrawal failed. Minimum balance of Rs.500 must remain.")
        return
    acc[2] = acc[2] - amount
    save_accounts(accounts)
    print("Withdrawal successful. Balance:", acc[2])


def transfer_money(accounts):
    from_no = read_number("From account: ")
    sender = find_account(accounts, from_no)
    if sender is None:
        print("Account", from_no, "not found. Transfer cancelled.")
        return
    to_no = read_number("To account: ")
    receiver = find_account(accounts, to_no)
    if receiver is None:
        print("Account", to_no, "not found. Transfer cancelled.")
        return
    if from_no == to_no:
        print("Cannot transfer to the same account. Transfer cancelled.")
        return
    amount = read_amount("Transfer amount: ")
    if sender[2] - amount < MIN_BALANCE:
        print("Transfer failed. Minimum balance of Rs.500 must remain.")
        return
    sender[2] = sender[2] - amount
    receiver[2] = receiver[2] + amount
    save_accounts(accounts)
    print("Transfer successful.", from_no, "balance:", sender[2],
          "|", to_no, "balance:", receiver[2])


def check_balance(accounts):
    acc_no = read_number("Account number: ")
    acc = find_account(accounts, acc_no)
    if acc is None:
        print("Account", acc_no, "not found.")
        return
    print("A/C No:", acc[0], "| Name:", acc[1], "| Balance:", acc[2])


# ---------- MAIN PROGRAM ----------

def main():
    while True:
        accounts = load_accounts()   # load latest data from the file

        print("\n===== SIMPLE BANKING SYSTEM =====")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Balance enquiry")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_money(accounts)
        elif choice == "3":
            withdraw_money(accounts)
        elif choice == "4":
            transfer_money(accounts)
        elif choice == "5":
            check_balance(accounts)
        elif choice == "6":
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


main()
