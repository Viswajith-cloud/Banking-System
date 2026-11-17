Simple Banking System

## Project summary

This project is a console-based banking application written in Python 3. It lets customers create accounts, deposit and withdraw money, transfer funds between accounts, and check account balances. Account records are stored in the text file `bank.txt` so they can be loaded again when the program is run later.

## Features

- Creates accounts with sequential account numbers beginning at **1001**.
- Requires a valid customer name and an opening deposit of at least **Rs. 500**.
- Supports deposits, withdrawals, transfers, and balance enquiries.
- Keeps at least **Rs. 500** in an account after a withdrawal or transfer.
- Checks that account numbers exist and rejects invalid menu choices and non-positive or non-numeric amounts.
- Prevents transfers to the same account and cancels a transfer if either account is not found.
- Saves account data as comma-separated records in `bank.txt` (`account number,name,balance`).

## How it works

The program loads the account file at the start of each menu cycle. Helper functions locate accounts, generate the next account number, and read positive whole-number amounts. Banking operations update the in-memory account records and save them back to `bank.txt` when a change succeeds. The menu continues until the user selects **Exit**.

## Running the program

1. Make sure Python 3 is installed.
2. Open a terminal in the folder containing `banking_system (1).py`.
3. Run:

   ```bash
   python "banking_system (1).py"
   ```

The `bank.txt` file is created in the program's current working directory when account data is first saved.

## Project brief and implementation

The implementation covers the brief's required functions: account creation, deposits, withdrawals, transfers, balance enquiry, input validation, the Rs. 500 minimum balance rule, and file-based persistence. The stated examples align with the program's behavior: an opening deposit of Rs. 2,000 creates account 1001 when no accounts exist; withdrawing Rs. 1,500 from a Rs. 2,000 balance leaves Rs. 500; a transfer to a missing account is cancelled; and a valid transfer updates both account balances.

## Scope

This is a small learning project intended for console use. It stores records in a plain text file and does not include authentication, encryption, transaction history, or database-backed storage.
