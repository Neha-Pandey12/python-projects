from typing import List
import datetime

class InsufficientFundError(Exception):
    pass

class Account:
    def __init__(self,owner:str,opening_balance:float=0.0,mini_limit:int=5):
        self.owner=owner
        self._balance=float(opening_balance)
        self._mini_limit=int(mini_limit)
        self._mini_statement:List[str]=[]

    def _record(self,description:str)->None:
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry=f"{timestamp} | {description}"
        self._mini_statement.append(entry)
        if len(self._mini_statement)>self._mini_limit:
            self._mini_statement.pop(0)
    def deposit(self,amount:float)->float:
        if amount<=0:
            raise ValueError("Deposit amount must be positive.")
        self._balance+=amount
        self._record(f"Deposit: +{amount:.2f} | Balance: {self._balance:.2f}")
        return self._balance
    
    def withdraw(self,amount:float)->float:
        if amount<=0:
            raise ValueError("withdrawal amount must be positive.")
        if amount>self._balance:
            raise InsufficientFundError(f"Insufficient funds: attempted to withdraw{amount:.2f},available {self._balance:.2f}")
        self._balance-=amount
        self._record(f"withdraw:-{amount:.2f} | Balance: {self._balance:.2f}")
        return self._balance
    
    def get_balance(self)->float:
        return float(self._balance)
    
    def mini_statement(self)->List[str]:
        return list(reversed(self._mini_statement))

def main():
    print("Simple ATM Simulator")
    name=input("enter account owner name:").strip() or "User"
    acct=Account(owner=name,opening_balance=0.0,mini_limit=5)

    menu=(
        "\nChoose an option:\n"
        "1) Check balance\n"
        "2) Deposit\n"
        "3) Withdraw\n"
        "4) Mini-statement\n"
        "5) Exit\n"
        "Enter choice: "
    )
    
    while True:
        choice=input(menu).strip()
        if choice=="1":
            print(f"current balance:Rs {acct.get_balance():.2f}")
        elif choice=="2":
            try:
                amt=float(input("Enter deposit amount:").strip())
                new_bal=acct.deposit(amt)
                print(f"Deposited {amt:.2f}. New balance:Rs {new_bal:2f}")
            except ValueError as ve:
                print("Error:",ve)
        elif choice=="3":
            try:
                amt=float(input("Enter withdrawal amount:").strip())
                new_bal=acct.withdraw(amt)
                print(f"withdrawm{amt:.2f}. New balance:Rs{new_bal:.2f}")
            except ValueError as ve:
                print("Error:",ve)
            except InsufficientFundError as ie:
                print("Transaction failed:",ie)
        elif choice=="4":
            print("\n---Mini-Statement(most recent first)---")
            entries=acct.mini_statement()
            if not entries:
                print("No transaction yet.")
            else:
                for e in entries:
                    print(e)
            print("------------------------------------------")

        elif choice=="5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.Try again.")
if __name__=="__main__":
    main()