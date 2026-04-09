"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from client.client import Client
from email_validator import validate_email, EmailNotValidError

class TestClient(unittest.TestCase):
    """Unit tests for the Client class."""

    def test_valid_client(self):
        """Test creating a Client with valid data."""
        #arrange
        client_number = 34
        first_name = "rown"
        last_name = "kate"
        email = "kateR@pixell.com"

        #act
        client = Client(client_number, first_name, last_name, email)

        #assert
        self.assertEqual(client._Client__client_number, client_number)
        self.assertEqual(client._Client__first_name, first_name) 
        self.assertEqual(client._Client__last_name, last_name)
        self.assertEqual(client._Client__email, email)

    def test_invalid_client_number(self):
        """Test creating a Client with a non-integer client number."""
        #arrange
        client_number = "34a"
        first_name = "rown"
        last_name = "kate"
        email = "kateR@pixell.com"

        #act
        with self.assertRaises(ValueError) as context:
            Client(client_number, first_name, last_name, email)

        #assert
        self.assertEqual(str(context.exception)
, "Client number must be an integer.")
        
    def test_blank_first_name(self):
        """Test creating a Client with a blank first name."""
        #arrange
        client_number = 34
        first_name = "   "
        last_name = "kate"
        email = "kateR@pixell.com"

        #act
        with self.assertRaises(ValueError) as context:
            Client(client_number, first_name, last_name, email)

        #assert
        self.assertEqual(str(context.exception)
, "First name must not be blank.")
        
    def test_blank_last_name(self):
        """Test creating a Client with a blank last name."""
        #arrange
        client_number = 34
        first_name = "rown"
        last_name = "   "
        email = "kateR@pixell.com"

        #act
        with self.assertRaises(ValueError) as context:
            Client(client_number, first_name, last_name, email)
        #assert
        self.assertEqual(str(context.exception)
, "Last name must not be blank.")
        
    def test_invalid_email(self):
        """Test creating a Client with an invalid email address."""
        #arrange
        client_number = 34
        first_name = "rown"
        last_name = "kate"
        email = "kateRpixell.com" 

        #act
        with self.assertRaises(ValueError) as context:
            Client(client_number, first_name, last_name, email)

        #assert
        self.assertTrue("Invalid email address" in str(context.exception))

    def test_client_number_property(self):
        """Test the client_number property."""
        #arrange
        client_number = 34
        first_name = "rown"
        last_name = "kate"
        email = "kateR@pixell.com"

        #act
        client = Client(client_number, first_name, last_name, email)
        returned_client_number = client.client_number

        #assert
        self.assertEqual(client.client_number, client_number)

    def test_first_name_property(self):
        """Test the first_name property."""
        #arrange
        client_number = 34
        first_name = "rown"
        last_name = "kate"
        email = "kateR@pixell.com"

        #act
        client = Client(client_number, first_name, last_name, email)
        returned_first_name = client.first_name

        #assert
        self.assertEqual(returned_first_name, first_name)

    def test_last_name_property(self):
        """Test the last_name property."""
        #arrange
        client_number = 34
        first_name = "rown"
        last_name = "kate"
        email = "kateR@pixell.com"

        #act
        client = Client(client_number, first_name, last_name, email)
        returned_last_name = client.last_name

        #assert
        self.assertEqual(returned_last_name, last_name)

    def test_email_property(self):
        """Test the email property."""
        #arrange
        client_number = 34
        first_name = "rown"
        last_name = "kate"
        email = "kateR@pixell.com"

        #act
        client = Client(client_number, first_name, last_name, email)
        returned_email = client.email

        #assert
        self.assertEqual(returned_email, email)

    def test_str_method(self):
        """Test the str method."""
        #arrange
        client_number = 34
        first_name = "rown"
        last_name = "kate"
        email = "kateR@pixell.com"

        #act
        client = Client(client_number, first_name, last_name, email)
        client_str = str(client)
        
        #assert
        self.assertEqual(client_str, "kate, rown [34]\n- kateR@pixell.com")

if __name__ == "__main__":
    unittest.main()

        
                        