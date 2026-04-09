<<<<<<< HEAD
# Secure-Project
=======
# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Gurkaran singh

## Assignment
Assignment [1]- BankAccount and Client Classes  
This assignment contains bank account and client classes and unittest for ensuring proper working.

## Encapsulation
1. private attribute

- The class establishes its fundamental data (`__account_number`, `__client_number`, `__balance`) as private attributes by utilizing double underscores.

- This stops external modification of sensitive data within the class.

2. Attributes

- Public `@property` methods (account_number, client_number, balance) provide regulated read-only access to private attributes.

3. Mutators

- Balance modifications happen solely via functions such as deposit(), withdraw(), and `update_balance().

4. Validation

`__init__ verifies that the account number and client number are integers, and ensures that the balance is numeric.

5. strings

- The `__str__()` function offers a structured, easily interpretable presentation of account information without revealing raw attribute identifiers.
>>>>>>> b3b9d29 (project setup)
