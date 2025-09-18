# -----------------------------
# Class Definition
# -----------------------------
class BankAccount:
    """A simple bank account class."""

    def __init__(self, owner: str, balance: float = 0):
        """
        Initialize a BankAccount instance.

        Args:
            owner (str): Name of the account owner.
            balance (float): Initial balance (default is 0).
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Deposit an amount into the account.
        """
        self.balance += amount
        print(f"The amount {amount} has been deposited. Current balance: {self.balance}")

    def check_balance(self) -> float:
        """
        Return the current balance.
        """
        return self.balance

    def withdraw(self, amount: float) -> None:
        """
        Withdraw an amount from the account if funds are sufficient.
        """
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"The amount {amount} has been withdrawn. Current balance: {self.balance}")

# ----------------------------- 
# # Helper Functions # 
# ----------------------------- 
def demo_accounts():
    """
    Demonstrate BankAccount operations using sample accounts.
    
    """



# 1. Sufficient funds – normal operations
acc1 = BankAccount('Peter', 5000) 
print(f"Owner: {acc1.owner}") 
acc1.withdraw(3000) 
acc1.deposit(10000)

# 2. Insufficient funds – error handling
acc2 = BankAccount('Jay', 1000)
print(f"\nOwner: {acc2.owner}")
acc2.withdraw(5000)          
acc2.deposit(2000)           
acc2.withdraw(1500)        
print(f"Final balance: {acc2.check_balance()}")

# 3. Default balance – optional argument test
acc3 = BankAccount('Tyler')  
print(f"\nOwner: {acc3.owner}")
print(f"Initial balance: {acc3.check_balance()}")
acc3.deposit(5000)            
print(f"Updated balance: {acc3.check_balance()}")

# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    demo_accounts()
