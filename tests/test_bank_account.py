"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_init_valid_inputs(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = 1067.50

        # Act
        account = BankAccount(account_number, client_number, balance)

        # Assert
        self.assertEqual(account._BankAccount__account_number, account_number)
        self.assertEqual(account._BankAccount__client_number, client_number)
        self.assertEqual(account._BankAccount__balance, balance)

    def test_balance_set_to_zero_when_non_numeric(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = "twenty thousand"

        # Act
        account = BankAccount(account_number, client_number, balance)

        # Assert
        self.assertEqual(account._BankAccount__balance, 0.0)

    def test_value_error_when_non_numeric_account_number(self):
        # Arrange
        account_number = "90876a"
        client_number = 7
        balance = 1067.50

        # Act
        with self.assertRaises(ValueError) as context:
            BankAccount(account_number, client_number, balance)
        
        # Assert
        self.assertEqual(str(context.exception), "Account number must be an integer.")

    def test_value_error_when_non_numeric_client_number(self):
        # Arrange
        account_number = 90876
        client_number = "7b"
        balance = 1067.50

        # Act
        with self.assertRaises(ValueError) as context:
            BankAccount(account_number, client_number, balance)
        
        # Assert
        self.assertEqual(str(context.exception), "Client number must be an integer.")

    def test_account_number(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = 1067.50
        account = BankAccount(account_number, client_number, balance)

        # Act
        result = account.account_number

        # Assert
        self.assertEqual(result, account_number)

    def test_client_number(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = 1067.50
        account = BankAccount(account_number, client_number, balance)

        # Act
        result = account.client_number

        # Assert
        self.assertEqual(result, client_number)

    def test_balance(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = 1067.50
        account = BankAccount(account_number, client_number, balance)

        # Act
        result = account.balance

        # Assert
        self.assertEqual(result, balance)

    def test_update_balance_with_positive_amount(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = 1067.50
        amount = 250.75
        account = BankAccount(account_number, client_number, balance)

        # Act
        account.update_balance(amount)

        # Assert
        self.assertEqual(account._BankAccount__balance, balance + amount)

    def test_update_balance_with_negative_amount(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = 1067.50
        amount = -109.00
        account = BankAccount(account_number, client_number, balance)

        # Act
        account.update_balance(amount)

        # Assert
        self.assertEqual(account._BankAccount__balance, balance + amount)

    def test_update_balance_with_non_numeric(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = 1067.50
        amount = "three hundred"
        account = BankAccount(account_number, client_number, balance)

        # Act
        account.update_balance(amount)

        # Assert
        self.assertEqual(account._BankAccount__balance, balance)

    def test_deposit_valid_amount(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = 1067.50
        amount = 309.00
        account = BankAccount(account_number, client_number, balance)

        # Act
        account.deposit(amount)

        # Assert
        self.assertEqual(account._BankAccount__balance, balance + amount)

    def test_deposit_negative_amount_raises_value_error(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = 1067.50
        amount = -309.00
        account = BankAccount(account_number, client_number, balance)

        # Act
        with self.assertRaises(ValueError) as context:
            account.deposit(amount)

        # Assert
        formatted_amount = f"${amount:,.2f}"
        self.assertEqual(
            str(context.exception),
            f"Deposit {formatted_amount} must be positive."
        )

    def test_withdraw_valid_amount(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = 1067.50
        amount = 309.00
        account = BankAccount(account_number, client_number, balance)

        # Act
        account.withdraw(amount)

        # Assert
        self.assertEqual(account._BankAccount__balance, balance - amount)

    def test_withdraw_negative_amount_raises_value_error(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = 1067.50
        amount = -309.00
        account = BankAccount(account_number, client_number, balance)

        # Act
        with self.assertRaises(ValueError) as context:
            account.withdraw(amount)

        # Assert
        formatted_amount = f"${amount:,.2f}"
        self.assertEqual(
            str(context.exception),
            f"Withdraw {formatted_amount} must be positive."
        )

    def test_withdraw_amount_exceeds_balance_raises_value_error(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = 1067.50
        amount = 1500.00
        account = BankAccount(account_number, client_number, balance)

        # Act
        with self.assertRaises(ValueError) as context:
            account.withdraw(amount)

        # Assert
        formatted_amount = f"${amount:,.2f}"
        formatted_balance = f"${balance:,.2f}"
        self.assertEqual(
            str(context.exception),
            f"Withdraw amount: {formatted_amount} must not exceed "
            f"the account balance: {formatted_balance}."
        )

    def test_str_representation(self):
        # Arrange
        account_number = 90876
        client_number = 7
        balance = 1067.50
        account = BankAccount(account_number, client_number, balance)

        # Act
        result = str(account)

        # Assert
        self.assertEqual(
            result,
            f"Account Number: {account_number}\n"
            f"Balance: ${balance:,.2f}"
        )