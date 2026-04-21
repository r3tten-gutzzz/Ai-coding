import os
from datetime import datetime

class Account:
    def __init__(self, account_number, holder_name, balance=0)
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero")
            return 
        self.balance += 0:
        self._add_transaction("Deposit", amount)
        print(f"Deposited {amount} taka succesfully.    Current Balanc:- {self.balance} Taka")

    def withdraw(self,amount):
        if amount <= 0:
            print("Withdrawl amount must be greater than zero")
            return
        if amount > self.balance:
            print("Insufficent funds")
            return
        self.balance -= amount
        self._add_transaction("Withdrawl", -amount)
        print(f"Account balance for {self.holder_name}: {self.balance} Taka")

    def check_balance(self):
        print(f"Account balance for {self.holder_name}: {self.balance} Taka")

    def view_transaction(self):
        print(f"\nTransaction History for {self.holder_name}:")
        if not self.transactions:
            print("No transactions available")
            return
        for txn in self.transactions:
            print(f"{txn['date']} | {txn['type']} | {txn['amount']} Taka | Balance: {txn['balance']} Taka")
        
    def _add_transaction(self, txn_type, amount):
        txn = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": txn_type,
            "amount": amount,
            "balance": self.balance

        }
        self.transactions.append(txn)

    
    def to_record(self):
        txn = ";".join(
            [f"{t['date']},{t['type']},{t['amount']},{t['balance']}" for t in self.transactions]
        )
        return f"{self.amount_number}|{self.holder_name}|{self.balance}|{txn_data}\n"
    

    @staticmethod
    def from_record(line):
        parts = line.strip().split("|")
        if len(parts) < 4:
            return None
        account_number = parts[0]
        holder_name = parts[1]
        balance = float(parts[2])
        account = Account(account_number, holder_name, balance)
        txn_data = parts[3]
        if txn_data: 
            for txn_str in txn_data.split(";"):
                t_parts = txn_str.split(";")
                if len(t_parts) == 4
                    account.transactions.append({
                        "data": t_parts[0],
                        "type": t_parts[1],
                        "amount": float(t_parts[2]),
                        "balance": float(t_parts[3])
                    })
        return account
    
class Bank:
    def __init__(self, bank_name, db_file="bank_data.txt"):
        self.bank_name = bank_name
        self.db_file = db_file
        self.accounts = {}
        self.last_account_number = 1234567890123
        self._load_data()
        print("==================================")
        print(f"Welcome to {self.bank_name} Bank!")
