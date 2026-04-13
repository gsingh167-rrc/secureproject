"""BANK ACCOUNT MODULE"""

__author__ = "Gurkaran singh"
__version__ = "1.0.0"

class BankAccount:
    """bank account class representing depost,withdraw and balance"""

    def __init__(self, account_number: int, client_number: int, balance: float):
        """Initialize a BankAccount instance.

        Args:
            account_number (int): bank account number
            client_number (int): number for account
            balance (float): Initial balance of the account.
        """

        # validate account number
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")

        #validate client number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")

        # validate balance
        try:
            balance = float(balance)
        except ValueError:
            balance = 0.0

        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance

    @property
    def account_number(self) -> int:
        """The account number of the bank account.

        Returns:
            int: The account number of the bank account.
        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """The client number of bank account

        Returns:
            int: The client number of bank account.
        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """The balance of the bank account.

        Returns:
            float: The balance of the bank account.
        """
        return self.__balance
    
    def update_balance(self, amount: float) -> None:
        """Update the balance of the bank account.

        Args:
            amount (float): The amount to add to the balance. 
        """
        try:
            amount = float(amount)
        except ValueError:
            return
        self.__balance += amount

    def deposit(self, amount: float) -> None:
        """Deposit money into the bank account.

        Args:
            amount (float): The amount to deposit.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit {amount} must be a numeric.")
        
        if amount <= 0:
            formatted_amount = f"${amount:,.2f}"
            raise ValueError(f"Deposit {formatted_amount} must be positive.")
        
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the bank account.

        Args:
            amount (float): The amount to withdraw.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw {amount} must be a numeric.")
        
        if amount <= 0:
            formatted_amount = f"${amount:,.2f}"
            raise ValueError(f"Withdraw {formatted_amount} must be positive.")
        
        if amount > self.__balance:
            formatted_amount = f"${amount:,.2f}"
            formatted_balance = f"${self.__balance:,.2f}"
            raise ValueError (f"Withdraw amount: {formatted_amount} must not exceed "
        f"the account balance: {formatted_balance}.") 

        self.update_balance(-amount)

    def __str__(self) -> str:
        """String representation of the bank account.

        Returns:
            str: String representation of the bank account.
        """
        formatted_balance = f"${self.__balance:,.2f}"
        return (f"Account Number: {self.__account_number}\n" 
                f"Balance: {formatted_balance}")

# peer review

#peer review completed
