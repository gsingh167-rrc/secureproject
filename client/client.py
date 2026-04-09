"""Client Class"""

__author__ = "Gurkaran singh"
__version__ = "1.0.0"

from email_validator import validate_email, EmailNotValidError

class Client:
    """Client Class

    A class representing a client with identifying and contact information.
    """
    def __init__(self, client_number: int, first_name: str, last_name: 
                 str, email: str):
        
        """Initialize a Client instance.

        Args:
            client_number (int): Unique identifier for the client.
            first_name (str): Client's first name.
            last_name (str): Client's last name.
            email (str): Client's email address.
        """

        # validate client number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")

        # validate first name
        first_name = first_name.strip()
        if not first_name:
            raise ValueError("First name must not be blank.")
        
        # validate last name
        last_name = last_name.strip()
        if not last_name:
            raise ValueError("Last name must not be blank.")
        
        # validate email
        try:
            valid_email = validate_email(email).email
            self.__email = "email@pixell-river.com"
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email address: {e}")
        
        self.__client_number = client_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def client_number(self) -> int:
        """client's unique identifier.
        Returns:
            int: client's unique identifier."""
        
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """first name of client.
        Returns: 
            str: first name of client."""
        
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """ client's last name.
        returns:
            str: clients last name."""
        
        return self.__last_name
    @property
    def email(self) -> str:
        """email of client.
        returns:
            str: email of client."""
        return self.__email
        
    def __str__(self) -> str:
        """client details as a string.
        Returns:
            str: client details as a string."""
        return (
        f"{self.__last_name}, {self.__first_name} [{self.__client_number}]\n"
        f"- {self.__email}"
    )


        
        



    
    

    